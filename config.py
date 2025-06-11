"""
Configuration settings for the SAP HANA SQL Analyzer Streamlit App
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # Azure OpenAI Configuration
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "https://models.inference.ai.azure.com")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "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")
    AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL", "gpt-4o")
    
    # Google Gemini Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = "gemini-2.5-flash-preview-04-17"
    
    # App Configuration
    DEFAULT_LLM_PROVIDER = os.getenv("DEFAULT_LLM_PROVIDER", "azure")
    MAX_PROCEDURES = int(os.getenv("MAX_PROCEDURES", "100"))
    ANALYSIS_TIMEOUT = int(os.getenv("ANALYSIS_TIMEOUT", "300"))
    
    # Streamlit Configuration
    PAGE_TITLE = "SAP HANA SQL Analyzer"
    PAGE_ICON = "🔍"
    LAYOUT = "wide"
    
    # File Upload Configuration
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = ['.sql', '.hdbprocedure', '.txt']
    
    # Analysis Configuration
    BATCH_SIZE = 10  # Process procedures in batches
    
    @classmethod
    def validate_config(cls):
        """Validate configuration settings"""
        issues = []
        
        if not cls.AZURE_OPENAI_API_KEY or cls.AZURE_OPENAI_API_KEY == "your_azure_api_key_here":
            issues.append("Azure OpenAI API key not configured")
        
        if not cls.GEMINI_API_KEY or cls.GEMINI_API_KEY == "your_gemini_api_key_here":
            issues.append("Gemini API key not configured")
        
        return issues
