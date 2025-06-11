"""
Robust LLM Service with Azure OpenAI and Google Gemini Support
=============================================================

This module provides a unified interface for multiple LLM providers
with robust error handling, retry logic, and fallback mechanisms.
"""

import os
import time
import json
import requests
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from google import genai
from google.genai import types
import streamlit as st
from config import Config

@dataclass
class LLMResponse:
    """Standardized LLM response"""
    content: str
    provider: str
    model: str
    success: bool
    error: Optional[str] = None
    tokens_used: Optional[int] = None
    response_time: Optional[float] = None

class LLMService:
    """Unified LLM service supporting multiple providers"""
    
    def __init__(self):
        self.config = Config()
        self.providers = {
            'azure': self._call_azure_openai,
            'gemini': self._call_gemini
        }
        
        # Initialize clients
        self.azure_headers = {
            "Authorization": f"Bearer {self.config.AZURE_OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        self.gemini_client = None
        if self.config.GEMINI_API_KEY:
            try:
                self.gemini_client = genai.Client(api_key=self.config.GEMINI_API_KEY)
            except Exception as e:
                st.warning(f"Failed to initialize Gemini client: {e}")
    
    def generate_requirements(self, 
                            analysis_data: Dict[str, Any], 
                            provider: str = "azure",
                            custom_prompt: Optional[str] = None) -> LLMResponse:
        """Generate requirements documentation from SQL analysis"""
        
        # Prepare the prompt
        system_prompt = self._get_system_prompt()
        user_prompt = custom_prompt or self._get_default_user_prompt(analysis_data)
        
        # Try primary provider
        response = self._call_llm_with_retry(provider, system_prompt, user_prompt)
        
        # Fallback to other provider if primary fails
        if not response.success:
            fallback_provider = 'gemini' if provider == 'azure' else 'azure'
            st.warning(f"Primary LLM ({provider}) failed, trying fallback ({fallback_provider})")
            response = self._call_llm_with_retry(fallback_provider, system_prompt, user_prompt)
        
        return response
    
    def _call_llm_with_retry(self, provider: str, system_prompt: str, user_prompt: str, max_retries: int = 3) -> LLMResponse:
        """Call LLM with retry logic"""
        
        if provider not in self.providers:
            return LLMResponse(
                content="", 
                provider=provider, 
                model="unknown", 
                success=False, 
                error=f"Unsupported provider: {provider}"
            )
        
        for attempt in range(max_retries):
            try:
                start_time = time.time()
                response = self.providers[provider](system_prompt, user_prompt)
                response.response_time = time.time() - start_time
                
                if response.success:
                    return response
                
                # Wait before retry
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    return LLMResponse(
                        content="", 
                        provider=provider, 
                        model="unknown", 
                        success=False, 
                        error=f"Failed after {max_retries} attempts: {str(e)}"
                    )
                time.sleep(2 ** attempt)
        
        return LLMResponse(
            content="", 
            provider=provider, 
            model="unknown", 
            success=False, 
            error="Max retries exceeded"
        )
    
    def _call_azure_openai(self, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Call Azure OpenAI API"""
        
        if not self.config.AZURE_OPENAI_API_KEY:
            return LLMResponse(
                content="", 
                provider="azure", 
                model=self.config.AZURE_OPENAI_MODEL, 
                success=False, 
                error="Azure OpenAI API key not configured"
            )
        
        try:
            data = {
                "model": self.config.AZURE_OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "max_tokens": 4000,
                "temperature": 0.7
            }
            
            response = requests.post(
                f"{self.config.AZURE_OPENAI_ENDPOINT}/chat/completions",
                headers=self.azure_headers,
                json=data,
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                tokens_used = result.get('usage', {}).get('total_tokens', 0)
                
                return LLMResponse(
                    content=content,
                    provider="azure",
                    model=self.config.AZURE_OPENAI_MODEL,
                    success=True,
                    tokens_used=tokens_used
                )
            else:
                return LLMResponse(
                    content="", 
                    provider="azure", 
                    model=self.config.AZURE_OPENAI_MODEL, 
                    success=False, 
                    error=f"API Error: {response.status_code} - {response.text}"
                )
                
        except Exception as e:
            return LLMResponse(
                content="", 
                provider="azure", 
                model=self.config.AZURE_OPENAI_MODEL, 
                success=False, 
                error=str(e)
            )
    
    def _call_gemini(self, system_prompt: str, user_prompt: str) -> LLMResponse:
        """Call Google Gemini API"""
        
        if not self.gemini_client:
            return LLMResponse(
                content="", 
                provider="gemini", 
                model=self.config.GEMINI_MODEL, 
                success=False, 
                error="Gemini client not initialized"
            )
        
        try:
            # Combine system and user prompts for Gemini
            combined_prompt = f"{system_prompt}\n\n{user_prompt}"
            
            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=combined_prompt)],
                ),
            ]
            
            generate_content_config = types.GenerateContentConfig(
                response_mime_type="text/plain",
                max_output_tokens=4000,
                temperature=0.7
            )
            
            # Use streaming for better handling
            response_text = ""
            for chunk in self.gemini_client.models.generate_content_stream(
                model=self.config.GEMINI_MODEL,
                contents=contents,
                config=generate_content_config,
            ):
                if chunk.text:
                    response_text += chunk.text
            
            return LLMResponse(
                content=response_text,
                provider="gemini",
                model=self.config.GEMINI_MODEL,
                success=True
            )
            
        except Exception as e:
            return LLMResponse(
                content="", 
                provider="gemini", 
                model=self.config.GEMINI_MODEL, 
                success=False, 
                error=str(e)
            )
    
    def _get_system_prompt(self) -> str:
        """Get system prompt for OTC migration analysis"""
        return """You are an expert SAP SQL/code analyst specializing in Order-to-Cash (OTC) process analysis and Celonis EMS migration projects. You have deep expertise in:

- SAP HANA SQL procedure analysis and optimization
- Order-to-Cash business process flows and data relationships
- Celonis EMS migration strategies and best practices
- Data volume analysis and performance optimization
- Complex join relationship mapping and filter pattern analysis

Your task is to analyze the provided SQL procedures related to Order-to-Cash (OTC) and produce a detailed analysis exactly matching the specified format for migration decision-making.

Focus on:
1. **Exact SQL Analysis** - Precise table names, join conditions, and filter patterns
2. **Data Volume Impact Assessment** - Quantify data reduction and performance implications
3. **Migration Decision Framework** - RETAIN/MODIFY/REVIEW with specific technical rationale
4. **Process Stage Mapping** - Map procedures to OTC business process stages
5. **Filter Pattern Optimization** - Identify consolidation opportunities across procedures
6. **Join Relationship Criticality** - Distinguish critical path vs. secondary reference joins

Provide exact field names, conditions, and technical details as they appear in the SQL code."""
    
    def _get_default_user_prompt(self, analysis_data: Dict[str, Any]) -> str:
        """Generate OTC-specific user prompt from analysis data"""

        # Extract key metrics
        summary = analysis_data.get('summary', {})
        table_consolidation = analysis_data.get('table_consolidation', {})
        filter_analysis = analysis_data.get('filter_analysis', {})
        join_analysis = analysis_data.get('join_analysis', {})

        # Format table consolidation data
        table_summary = []
        for table_name, table_data in table_consolidation.items():
            table_summary.append({
                'table': table_name,
                'procedures': table_data['used_in_procedures'],
                'procedure_count': table_data['procedure_count'],
                'filters': table_data['consolidated_filters'],
                'joins': table_data['consolidated_joins'],
                'priority': table_data['migration_priority']
            })

        prompt = f"""
Based on this comprehensive SAP HANA SQL procedure analysis for Order-to-Cash (OTC) Celonis EMS migration, produce a detailed analysis exactly matching this format:

## Analysis Input Data

### Procedure Summary
- **Total Procedures Analyzed**: {summary.get('total_procedures', 0)}
- **Unique Tables Identified**: {summary.get('unique_tables', 0)}
- **Total Join Relationships**: {summary.get('total_joins', 0)}
- **Total Filter Conditions**: {summary.get('total_filters', 0)}

### Table Consolidation Analysis
{json.dumps(table_summary, indent=2)}

### Filter Pattern Analysis
{json.dumps(filter_analysis, indent=2)}

### Join Pattern Analysis
{json.dumps(join_analysis, indent=2)}

## Required Output Format

### 1. Consolidated SQL Analysis Matrix for Order-to-Cash Process Procedures

| Procedure ID | Procedure Name | Source Tables | Key Joins | Key Filters | Aggregations/Transformations | Output Tables | Data Volume Impact | Migration Decision |
|--------------|---------------|--------------|-----------|------------|----------------------------|--------------|-------------------|-------------------|

For each procedure, provide:
- Procedure ID: Format OTC-XXX (sequential numbering)
- Procedure Name: Exact name from CREATE PROCEDURE statement
- Source Tables: All tables in FROM/JOIN clauses
- Key Joins: Exact join conditions (e.g., "INNER JOIN VBUK ON VBAK.MANDT = VBUK.MANDT AND VBAK.VBELN = VBUK.VBELN")
- Key Filters: All WHERE conditions with exact field names and values
- Aggregations/Transformations: Any CASE statements, calculations, or data modifications
- Output Tables: Target tables for INSERT/UPDATE operations
- Data Volume Impact: Show order of magnitude and reduction (e.g., "HIGH - 15M → ~2.7K (99.98% reduction)")
- Migration Decision: RETAIN/MODIFY/REVIEW with specific reason

### 2. Order-to-Cash Process Analysis for Celonis EMS Migration

#### Key Process Areas and Data Coverage
Create a table showing each process stage with:
- Process Stage names in bold
- Primary Tables used
- Exact join conditions between tables
- Critical filters that define business logic
- Business significance of each stage

### 3. Migration Considerations by Data Category
Group into:
1. Master Data (Customer, Material, Pricing)
2. Transaction Data (Orders, Deliveries, Billing)
3. Status & Control Data
For each category, state RETAIN/MODIFY/REVIEW with rationale.

### 4. Key Filter Patterns Across OTC
Document all filter patterns with:
- Pattern description (e.g., Date Filters)
- Usage frequency across procedures
- Exact field names and conditions used
- Recommendations for retention

### 5. Join Relationship Analysis
Document:
1. Critical Path Joins - Show exact field relationships
2. Secondary Reference Joins - Show exact join conditions
Include table and field names exactly as they appear in code.

### 6. Transformation Logic Analysis
Table showing:
| Transformation Type | Frequency | Example | Migration Consideration |
Include exact CASE statements and calculations from code.

Use the exact table names, field names, and conditions from the analysis data provided above.
"""

        return prompt
    
    def test_connection(self, provider: str) -> LLMResponse:
        """Test LLM provider connection"""
        test_prompt = "Respond with 'Connection successful' if you can process this request."
        
        return self._call_llm_with_retry(
            provider, 
            "You are a helpful assistant.", 
            test_prompt, 
            max_retries=1
        )
