"""
SAP HANA SQL Analyzer - Streamlit Web Application
================================================

A comprehensive web application for analyzing SAP HANA SQL procedures
and generating migration requirements documentation using LLMs.

Features:
- Upload and analyze multiple SQL procedures
- Advanced SQL parsing with migration insights
- Dual LLM support (Azure OpenAI + Google Gemini)
- Interactive visualizations and reports
- CSV and text file downloads
- Real-time analysis progress tracking
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import io
import zipfile
from datetime import datetime
from typing import List, Dict, Any, Optional

# Import our modules
from config import Config
from sql_parser import AdvancedSQLParser, ProcedureAnalysis
from llm_service import LLMService, LLMResponse

# Page configuration
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT,
    initial_sidebar_state="expanded"
)

class SAP_HANA_Analyzer_App:
    """Main Streamlit application class"""
    
    def __init__(self):
        self.config = Config()
        self.sql_parser = AdvancedSQLParser()
        self.llm_service = LLMService()
        
        # Initialize session state
        if 'analysis_results' not in st.session_state:
            st.session_state.analysis_results = None
        if 'llm_response' not in st.session_state:
            st.session_state.llm_response = None
        if 'procedures_data' not in st.session_state:
            st.session_state.procedures_data = []
    
    def run(self):
        """Main application entry point"""
        
        # Sidebar configuration
        self._render_sidebar()
        
        # Main content
        st.title("🔍 SAP HANA SQL Analyzer")
        st.markdown("**Advanced SQL Procedure Analysis for Migration Planning**")
        
        # Configuration validation
        config_issues = self.config.validate_config()
        if config_issues:
            st.warning("⚠️ Configuration Issues:")
            for issue in config_issues:
                st.write(f"- {issue}")
            st.info("Please check your API keys in the sidebar.")
        
        # Main tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📁 Upload & Analyze", 
            "📊 Analysis Results", 
            "🤖 LLM Requirements", 
            "📈 Visualizations"
        ])
        
        with tab1:
            self._render_upload_tab()
        
        with tab2:
            self._render_results_tab()
        
        with tab3:
            self._render_llm_tab()
        
        with tab4:
            self._render_visualizations_tab()
    
    def _render_sidebar(self):
        """Render sidebar with configuration options"""
        
        st.sidebar.header("⚙️ Configuration")
        
        # LLM Provider Selection
        st.sidebar.subheader("LLM Provider")
        provider = st.sidebar.selectbox(
            "Choose LLM Provider",
            options=["azure", "gemini"],
            index=0 if self.config.DEFAULT_LLM_PROVIDER == "azure" else 1,
            help="Select the LLM provider for requirements generation"
        )
        
        # Test LLM Connection
        if st.sidebar.button("🔍 Test LLM Connection"):
            with st.sidebar:
                with st.spinner(f"Testing {provider} connection..."):
                    response = self.llm_service.test_connection(provider)
                    if response.success:
                        st.success(f"✅ {provider.title()} connection successful!")
                    else:
                        st.error(f"❌ {provider.title()} connection failed: {response.error}")
        
        # API Configuration
        st.sidebar.subheader("API Configuration")
        
        if provider == "azure":
            azure_key = st.sidebar.text_input(
                "Azure OpenAI API Key",
                value=self.config.AZURE_OPENAI_API_KEY[:10] + "..." if self.config.AZURE_OPENAI_API_KEY else "",
                type="password",
                help="Your Azure OpenAI API key"
            )
            azure_model = st.sidebar.text_input(
                "Azure Model",
                value=self.config.AZURE_OPENAI_MODEL,
                help="Azure OpenAI model name"
            )
        else:
            gemini_key = st.sidebar.text_input(
                "Gemini API Key",
                value=self.config.GEMINI_API_KEY[:10] + "..." if self.config.GEMINI_API_KEY else "",
                type="password",
                help="Your Google Gemini API key"
            )
        
        # Analysis Settings
        st.sidebar.subheader("Analysis Settings")
        max_procedures = st.sidebar.number_input(
            "Max Procedures to Analyze",
            min_value=1,
            max_value=self.config.MAX_PROCEDURES,
            value=min(50, self.config.MAX_PROCEDURES),
            help="Maximum number of procedures to analyze in one batch"
        )
        
        # Store settings in session state
        st.session_state.selected_provider = provider
        st.session_state.max_procedures = max_procedures
        
        # Download Section
        st.sidebar.subheader("📥 Downloads")
        if st.session_state.analysis_results:
            self._render_download_buttons()
    
    def _render_upload_tab(self):
        """Render the upload and analysis tab"""
        
        st.header("📁 Upload SQL Procedures")
        
        # File upload options
        upload_method = st.radio(
            "Choose upload method:",
            ["Upload Files", "Paste SQL Text"],
            horizontal=True
        )
        
        procedures_data = []
        
        if upload_method == "Upload Files":
            uploaded_files = st.file_uploader(
                "Upload SQL procedure files",
                type=['sql', 'hdbprocedure', 'txt'],
                accept_multiple_files=True,
                help="Upload your SAP HANA SQL procedure files"
            )
            
            if uploaded_files:
                st.success(f"📁 {len(uploaded_files)} files uploaded")
                
                for file in uploaded_files:
                    try:
                        content = file.read().decode('utf-8')
                        procedures_data.append({
                            'name': file.name,
                            'content': content,
                            'size': len(content)
                        })
                    except Exception as e:
                        st.error(f"Error reading {file.name}: {e}")
        
        else:  # Paste SQL Text
            st.subheader("Paste SQL Procedure")
            
            procedure_name = st.text_input(
                "Procedure Name",
                placeholder="e.g., PR_GS_O2C_ADDRC_DELTA"
            )
            
            sql_content = st.text_area(
                "SQL Procedure Content",
                height=300,
                placeholder="Paste your SAP HANA SQL procedure here..."
            )
            
            if procedure_name and sql_content:
                procedures_data.append({
                    'name': procedure_name,
                    'content': sql_content,
                    'size': len(sql_content)
                })
        
        # Analysis section
        if procedures_data:
            st.subheader("🔍 Analysis")
            
            # Show procedure summary
            total_size = sum(p['size'] for p in procedures_data)
            st.info(f"📊 Ready to analyze {len(procedures_data)} procedures ({total_size:,} characters)")
            
            # Limit check
            max_procs = st.session_state.get('max_procedures', 50)
            if len(procedures_data) > max_procs:
                st.warning(f"⚠️ Too many procedures. Limiting to first {max_procs} procedures.")
                procedures_data = procedures_data[:max_procs]
            
            # Analysis button
            if st.button("🚀 Start Analysis", type="primary"):
                self._run_analysis(procedures_data)
    
    def _run_analysis(self, procedures_data: List[Dict[str, Any]]):
        """Run the SQL analysis"""
        
        with st.spinner("🔍 Analyzing SQL procedures..."):
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Parse procedures
                parsed_procedures = []
                
                for i, proc_data in enumerate(procedures_data):
                    status_text.text(f"Parsing procedure {i+1}/{len(procedures_data)}: {proc_data['name']}")
                    
                    try:
                        analysis = self.sql_parser.parse_procedure(
                            proc_data['content'], 
                            proc_data['name']
                        )
                        parsed_procedures.append(analysis)
                    except Exception as e:
                        st.error(f"Error parsing {proc_data['name']}: {e}")
                    
                    progress_bar.progress((i + 1) / len(procedures_data) * 0.7)
                
                # Cross-procedure analysis
                status_text.text("Performing cross-procedure analysis...")
                cross_analysis = self.sql_parser.analyze_cross_procedure_patterns(parsed_procedures)
                progress_bar.progress(0.9)
                
                # Store results
                st.session_state.analysis_results = {
                    'procedures': parsed_procedures,
                    'cross_analysis': cross_analysis,
                    'timestamp': datetime.now().isoformat()
                }
                st.session_state.procedures_data = procedures_data
                
                progress_bar.progress(1.0)
                status_text.text("✅ Analysis complete!")
                
                st.success(f"🎉 Successfully analyzed {len(parsed_procedures)} procedures!")
                
                # Show quick summary
                self._show_quick_summary(cross_analysis)
                
            except Exception as e:
                st.error(f"❌ Analysis failed: {e}")
                st.exception(e)
    
    def _show_quick_summary(self, cross_analysis: Dict[str, Any]):
        """Show quick analysis summary"""
        
        summary = cross_analysis.get('summary', {})
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Procedures", summary.get('total_procedures', 0))
        
        with col2:
            st.metric("Unique Tables", summary.get('unique_tables', 0))
        
        with col3:
            st.metric("Total Joins", summary.get('total_joins', 0))
        
        with col4:
            st.metric("Total Filters", summary.get('total_filters', 0))
    
    def _render_results_tab(self):
        """Render the analysis results tab"""
        
        if not st.session_state.analysis_results:
            st.info("📊 No analysis results yet. Please upload and analyze procedures first.")
            return
        
        st.header("📊 Analysis Results")
        
        results = st.session_state.analysis_results
        procedures = results['procedures']
        cross_analysis = results['cross_analysis']
        
        # Summary metrics
        st.subheader("📈 Summary Metrics")
        self._show_detailed_metrics(cross_analysis)
        
        # LLM-Generated Table Analysis
        st.subheader("📋 LLM-Generated Table Analysis")

        # Button to generate LLM table analysis
        if st.button("🤖 Generate LLM Table Analysis", key="generate_table_analysis"):
            with st.spinner("🤖 Generating LLM table analysis..."):
                table_analysis_response = self._generate_llm_table_analysis(cross_analysis)
                if table_analysis_response:
                    st.session_state.table_analysis_response = table_analysis_response

        # Show LLM table analysis if available
        if hasattr(st.session_state, 'table_analysis_response') and st.session_state.table_analysis_response:
            self._show_llm_table_analysis(st.session_state.table_analysis_response)

        # Fallback: Raw table analysis dataframe
        with st.expander("📊 Raw Parsed Data (for reference)", expanded=False):
            table_df = self._create_table_analysis_dataframe(procedures)

            if not table_df.empty:
                st.dataframe(
                    table_df,
                    use_container_width=True,
                    height=400
                )

                # Download button for table analysis
                csv_data = table_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Raw Table Analysis (CSV)",
                    data=csv_data,
                    file_name=f"table_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        # Filter analysis
        st.subheader("🔍 Filter Pattern Analysis")
        self._show_filter_analysis(cross_analysis.get('filter_analysis', {}))
        
        # Join analysis
        st.subheader("🔗 Join Pattern Analysis")
        self._show_join_analysis(cross_analysis.get('join_analysis', {}))
    
    def _create_table_analysis_dataframe(self, procedures: List[ProcedureAnalysis]) -> pd.DataFrame:
        """Create consolidated table analysis dataframe - ONE ROW PER TABLE"""

        # Get consolidated table analysis
        cross_analysis = st.session_state.analysis_results.get('cross_analysis', {})
        table_consolidation = cross_analysis.get('table_consolidation', {})

        if not table_consolidation:
            return pd.DataFrame()

        rows = []

        for table_name, table_data in table_consolidation.items():
            # Format procedures using this table
            procedures_str = ", ".join(table_data['used_in_procedures'])

            # Format all columns used across procedures
            columns_str = ", ".join([f"{table_name}.{col}" for col in table_data['all_columns']])

            # Format usage contexts
            used_as = ", ".join(table_data['usage_contexts'])

            # Consolidate filter conditions
            filter_info = table_data['consolidated_filters']
            if filter_info['has_filters']:
                filter_patterns = []
                for pattern in filter_info['patterns']:
                    example = pattern['example_conditions'][0] if pattern['example_conditions'] else ""
                    filter_patterns.append(f"{pattern['column']}: {example}")
                filter_conditions = " | ".join(filter_patterns)
            else:
                filter_conditions = ""

            # Consolidate join conditions
            join_info = table_data['consolidated_joins']
            if join_info['has_joins']:
                join_patterns = []
                for rel in join_info['relationships']:
                    join_patterns.append(f"→ {rel['related_table']}: {rel['example_condition']}")
                join_conditions = " | ".join(join_patterns)
            else:
                join_conditions = ""

            # Enhanced notes with migration info
            notes = f"{table_data['table_purpose']} | Used in {table_data['procedure_count']} procedures | Priority: {table_data['migration_priority']}"

            row = {
                'Table Name': table_name,
                'Used in Procedures': procedures_str,
                'Procedure Count': table_data['procedure_count'],
                'All Columns Used': columns_str,
                'Usage Contexts': used_as,
                'Consolidated Filters': filter_conditions,
                'Consolidated Joins': join_conditions,
                'Migration Priority': table_data['migration_priority'],
                'Notes': notes
            }
            rows.append(row)

        # Sort by migration priority and procedure count
        df = pd.DataFrame(rows)
        if not df.empty:
            priority_order = {'CRITICAL': 4, 'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
            df['priority_score'] = df['Migration Priority'].map(priority_order)
            df = df.sort_values(['priority_score', 'Procedure Count'], ascending=[False, False])
            df = df.drop('priority_score', axis=1)

        return df
    
    def _show_detailed_metrics(self, cross_analysis: Dict[str, Any]):
        """Show detailed metrics"""
        
        summary = cross_analysis.get('summary', {})
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Procedures", summary.get('total_procedures', 0))
            st.metric("Unique Tables", summary.get('unique_tables', 0))
        
        with col2:
            st.metric("Total Joins", summary.get('total_joins', 0))
            st.metric("Total Filters", summary.get('total_filters', 0))
    
    def _show_filter_analysis(self, filter_analysis: Dict[str, Any]):
        """Show filter pattern analysis"""
        
        if not filter_analysis:
            st.info("No filter analysis available")
            return
        
        # Recommendations
        recommendations = filter_analysis.get('recommendations', [])
        if recommendations:
            st.warning("⚠️ Migration Considerations:")
            for rec in recommendations:
                st.write(f"- {rec}")
        
        # Filter patterns summary
        summary = filter_analysis.get('summary', {})
        if summary:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Filtered Columns", summary.get('total_filtered_columns', 0))
            with col2:
                avg_coverage = summary.get('avg_filter_coverage', 0)
                st.metric("Avg Filter Coverage", f"{avg_coverage:.1f}%")
    
    def _show_join_analysis(self, join_analysis: Dict[str, Any]):
        """Show join pattern analysis"""
        
        if not join_analysis:
            st.info("No join analysis available")
            return
        
        # Complexity issues
        complexity_issues = join_analysis.get('complexity_issues', [])
        if complexity_issues:
            st.warning("⚠️ Join Complexity Issues:")
            for issue in complexity_issues:
                st.write(f"- {issue}")
        
        # Join patterns summary
        summary = join_analysis.get('summary', {})
        if summary:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Join Patterns", summary.get('total_join_patterns', 0))
            with col2:
                avg_procs = summary.get('avg_procedures_per_join', 0)
                st.metric("Avg Procedures per Join", f"{avg_procs:.1f}")
    
    def _render_llm_tab(self):
        """Render the LLM requirements generation tab"""
        
        if not st.session_state.analysis_results:
            st.info("🤖 Please complete the SQL analysis first to generate requirements.")
            return
        
        st.header("🤖 LLM Requirements Generation")
        
        # Provider selection
        provider = st.session_state.get('selected_provider', 'azure')
        st.info(f"Using {provider.title()} LLM provider")
        
        # Custom prompt option
        use_custom_prompt = st.checkbox("Use custom prompt")
        custom_prompt = None
        
        if use_custom_prompt:
            custom_prompt = st.text_area(
                "Custom Prompt",
                height=200,
                placeholder="Enter your custom prompt for requirements generation..."
            )
        
        # Generate requirements
        if st.button("🚀 Generate Requirements", type="primary"):
            self._generate_requirements(provider, custom_prompt)
        
        # Show previous results
        if st.session_state.llm_response:
            self._show_llm_results()
    
    def _generate_requirements(self, provider: str, custom_prompt: Optional[str]):
        """Generate requirements using LLM"""
        
        with st.spinner(f"🤖 Generating requirements using {provider.title()}..."):
            try:
                analysis_data = st.session_state.analysis_results['cross_analysis']
                
                response = self.llm_service.generate_requirements(
                    analysis_data=analysis_data,
                    provider=provider,
                    custom_prompt=custom_prompt
                )
                
                st.session_state.llm_response = response
                
                if response.success:
                    st.success(f"✅ Requirements generated successfully using {response.provider}!")
                    if response.response_time:
                        st.info(f"⏱️ Generation time: {response.response_time:.2f} seconds")
                else:
                    st.error(f"❌ Requirements generation failed: {response.error}")
                
            except Exception as e:
                st.error(f"❌ Error generating requirements: {e}")
                st.exception(e)
    
    def _show_llm_results(self):
        """Show LLM generation results with clean web display and download option"""

        response = st.session_state.llm_response

        if not response or not response.success:
            return

        st.subheader("📄 Generated OTC Migration Requirements")

        # Metadata in a compact format
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Provider", response.provider.title())
        with col2:
            st.metric("Model", response.model)
        with col3:
            if response.tokens_used:
                st.metric("Tokens Used", response.tokens_used)
        with col4:
            if response.response_time:
                st.metric("Response Time", f"{response.response_time:.1f}s")

        # Quick summary/preview
        st.markdown("---")
        self._show_requirements_summary(response.content)

        # Clean web display with proper formatting
        st.markdown("---")
        st.subheader("📋 Detailed Analysis")

        # Parse and display the content in a structured way
        self._display_formatted_requirements(response.content)

        # Download section
        st.markdown("---")
        st.subheader("📥 Download Options")

        col1, col2 = st.columns(2)

        with col1:
            # Download as TXT
            st.download_button(
                label="📄 Download as TXT",
                data=response.content,
                file_name=f"otc_migration_requirements_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                help="Download the complete requirements as a text file"
            )

        with col2:
            # Download as Markdown
            st.download_button(
                label="📝 Download as Markdown",
                data=response.content,
                file_name=f"otc_migration_requirements_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                help="Download the requirements as a Markdown file"
            )

    def _display_formatted_requirements(self, content: str):
        """Display the LLM requirements in a clean, formatted way"""

        # Split content into sections
        sections = self._parse_requirements_sections(content)

        if not sections:
            # Fallback: display as markdown if parsing fails
            st.markdown(content)
            return

        # Display each section with proper formatting
        for section_title, section_content in sections.items():

            if "matrix" in section_title.lower() or "table" in section_title.lower():
                # Display tables with special formatting
                st.subheader(section_title)
                self._display_requirements_table(section_content)

            elif "process areas" in section_title.lower():
                # Display process areas with expandable sections
                st.subheader(section_title)
                self._display_process_areas(section_content)

            elif "filter patterns" in section_title.lower():
                # Display filter patterns with highlighting
                st.subheader(section_title)
                self._display_filter_patterns(section_content)

            elif "join relationship" in section_title.lower():
                # Display join analysis with code formatting
                st.subheader(section_title)
                self._display_join_analysis(section_content)

            else:
                # Default section display
                st.subheader(section_title)
                st.markdown(section_content)

    def _parse_requirements_sections(self, content: str) -> Dict[str, str]:
        """Parse the LLM requirements into sections"""
        sections = {}

        # Split by headers (## or ###)
        lines = content.split('\n')
        current_section = None
        current_content = []

        for line in lines:
            if line.strip().startswith('##') or line.strip().startswith('###'):
                # Save previous section
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()

                # Start new section
                current_section = line.strip().lstrip('#').strip()
                current_content = []
            else:
                current_content.append(line)

        # Save last section
        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()

        return sections

    def _display_requirements_table(self, content: str):
        """Display requirements table with proper formatting"""

        # Look for markdown table
        lines = content.split('\n')
        table_lines = []
        in_table = False

        for line in lines:
            if '|' in line and line.strip():
                table_lines.append(line)
                in_table = True
            elif in_table and not line.strip():
                break

        if table_lines and len(table_lines) >= 2:
            try:
                # Parse markdown table
                headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]

                # Skip separator line
                data_rows = []
                for line in table_lines[2:]:
                    if '|' in line:
                        row = [cell.strip() for cell in line.split('|')[1:-1]]
                        if len(row) == len(headers):
                            data_rows.append(row)

                if data_rows:
                    # Create DataFrame and display
                    df = pd.DataFrame(data_rows, columns=headers)
                    st.dataframe(df, use_container_width=True)
                else:
                    st.markdown(content)
            except:
                st.markdown(content)
        else:
            st.markdown(content)

    def _display_process_areas(self, content: str):
        """Display process areas with expandable sections"""

        # Split into process stages
        lines = content.split('\n')
        current_stage = None
        current_details = []

        for line in lines:
            if line.strip().startswith('**') and line.strip().endswith('**'):
                # Save previous stage
                if current_stage:
                    with st.expander(current_stage, expanded=True):
                        st.markdown('\n'.join(current_details))

                # Start new stage
                current_stage = line.strip().strip('*')
                current_details = []
            else:
                current_details.append(line)

        # Save last stage
        if current_stage:
            with st.expander(current_stage, expanded=True):
                st.markdown('\n'.join(current_details))

        # If no stages found, display as markdown
        if not current_stage:
            st.markdown(content)

    def _display_filter_patterns(self, content: str):
        """Display filter patterns with highlighting"""

        # Look for filter pattern entries
        lines = content.split('\n')

        for line in lines:
            if line.strip():
                if 'Pattern:' in line or 'Filter:' in line:
                    st.info(line)
                elif 'RECOMMENDATION:' in line.upper():
                    st.success(line)
                elif 'RETAIN' in line.upper():
                    st.success(f"✅ {line}")
                elif 'REMOVE' in line.upper() or 'MODIFY' in line.upper():
                    st.warning(f"⚠️ {line}")
                elif 'REVIEW' in line.upper():
                    st.error(f"🔍 {line}")
                else:
                    st.markdown(line)

    def _display_join_analysis(self, content: str):
        """Display join analysis with code formatting"""

        lines = content.split('\n')

        for line in lines:
            if line.strip():
                if 'JOIN' in line.upper() and 'ON' in line.upper():
                    # Format SQL joins with code highlighting
                    st.code(line, language='sql')
                elif 'Critical Path' in line or 'Secondary Reference' in line:
                    st.subheader(line)
                else:
                    st.markdown(line)

    def _show_requirements_summary(self, content: str):
        """Show a quick summary of the requirements"""

        st.subheader("📊 Requirements Summary")

        # Extract key metrics from content
        lines = content.split('\n')

        # Count procedures, tables, etc.
        procedure_count = 0
        table_count = 0
        retain_count = 0
        modify_count = 0
        review_count = 0

        for line in lines:
            if 'OTC-' in line and '|' in line:
                procedure_count += 1
            if 'RETAIN' in line.upper():
                retain_count += 1
            elif 'MODIFY' in line.upper():
                modify_count += 1
            elif 'REVIEW' in line.upper():
                review_count += 1

        # Display summary metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Procedures Analyzed", procedure_count if procedure_count > 0 else "Multiple")

        with col2:
            st.metric("Migration Decisions", f"{retain_count + modify_count + review_count}")

        with col3:
            if retain_count > 0:
                st.metric("RETAIN", retain_count, delta="Safe to migrate")

        with col4:
            if modify_count + review_count > 0:
                st.metric("MODIFY/REVIEW", modify_count + review_count, delta="Needs attention")

        # Key recommendations preview
        recommendations = []
        for line in lines:
            if 'RECOMMENDATION:' in line.upper():
                recommendations.append(line.strip())

        if recommendations:
            st.subheader("🎯 Key Recommendations")
            for i, rec in enumerate(recommendations[:3], 1):  # Show top 3
                st.info(f"{i}. {rec}")

            if len(recommendations) > 3:
                st.caption(f"... and {len(recommendations) - 3} more recommendations below")

        # Migration complexity indicator
        complexity_indicators = ['CRITICAL', 'HIGH', 'COMPLEX', 'REVIEW']
        complexity_score = sum(1 for line in lines for indicator in complexity_indicators if indicator in line.upper())

        if complexity_score > 5:
            st.warning("🔴 High Complexity Migration - Requires detailed planning")
        elif complexity_score > 2:
            st.info("🟡 Medium Complexity Migration - Standard approach with some considerations")
        else:
            st.success("🟢 Low Complexity Migration - Straightforward implementation")

    def _generate_llm_table_analysis(self, cross_analysis: Dict[str, Any]):
        """Generate LLM-powered table analysis"""

        try:
            # Prepare data for LLM
            table_consolidation = cross_analysis.get('table_consolidation', {})
            filter_analysis = cross_analysis.get('filter_analysis', {})
            join_analysis = cross_analysis.get('join_analysis', {})

            # Create specific prompt for table analysis
            prompt = self._create_table_analysis_prompt(table_consolidation, filter_analysis, join_analysis)

            # Generate using LLM service
            response = self.llm_service.generate_requirements(
                analysis_data={'table_consolidation': table_consolidation},
                custom_prompt=prompt
            )

            return response

        except Exception as e:
            st.error(f"Failed to generate LLM table analysis: {e}")
            return None

    def _create_table_analysis_prompt(self, table_consolidation: Dict, filter_analysis: Dict, join_analysis: Dict) -> str:
        """Create specific prompt for table analysis"""

        # Format table data for LLM
        table_summary = []
        for table_name, table_data in table_consolidation.items():
            table_info = {
                'table': table_name,
                'procedures': table_data['used_in_procedures'],
                'columns': table_data['all_columns'],
                'filters': table_data['consolidated_filters'],
                'joins': table_data['consolidated_joins'],
                'priority': table_data['migration_priority']
            }
            table_summary.append(table_info)

        prompt = f"""
You are an expert SAP SQL analyst. Based on the ANTLR-parsed procedure data below, generate a comprehensive table analysis in the exact format requested.

## ANTLR Parsed Data:

### Table Consolidation Data:
{json.dumps(table_summary, indent=2)}

### Filter Analysis:
{json.dumps(filter_analysis, indent=2)}

### Join Analysis:
{json.dumps(join_analysis, indent=2)}

## Required Output Format:

Generate a detailed table analysis with the following sections:

### 1. Table-by-Table Analysis Matrix

Create a table with these exact columns:
| Table Name | Used in Procedures | All Columns | Filter Patterns | Join Relationships | Migration Priority | Notes |

For each table, provide:
- **Table Name**: SAP table name (BSEG, BKPF, VBAK, etc.)
- **Used in Procedures**: List of procedure names using this table
- **All Columns**: All columns used across procedures (e.g., BSEG.LIFNR, BSEG.DMBTR, BSEG.KOART)
- **Filter Patterns**: Exact filter conditions with procedure names
- **Join Relationships**: Exact join conditions with related tables
- **Migration Priority**: CRITICAL/HIGH/MEDIUM/LOW with rationale
- **Notes**: Business purpose and migration considerations

### 2. Column Usage Analysis

For each table, analyze:
- **Frequently Used Columns**: Columns used across multiple procedures
- **Procedure-Specific Columns**: Columns used in only one procedure
- **Filter Columns**: Columns that have filter conditions
- **Join Columns**: Columns used in join relationships

### 3. Migration Recommendations by Table

For each table provide:
- **Data Volume Impact**: Expected data volume and performance considerations
- **Filter Optimization**: Recommendations for filter consolidation
- **Join Optimization**: Recommendations for join performance
- **Migration Sequence**: Order of table migration based on dependencies

### 4. Critical Findings

Highlight:
- **Tables with Complex Logic**: Tables with multiple filter patterns or complex joins
- **High-Priority Tables**: Tables critical for business processes
- **Optimization Opportunities**: Areas where filters or joins can be improved

Focus on providing exact column names, filter conditions, and join relationships as they appear in the parsed data. Include specific procedure names and technical details for data engineers.
"""

        return prompt

    def _show_llm_table_analysis(self, response):
        """Display LLM-generated table analysis"""

        if not response or not response.success:
            st.error("Failed to generate table analysis")
            return

        st.subheader("🤖 LLM-Generated Table Analysis")

        # Show metadata
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Provider", response.provider.title())
        with col2:
            st.metric("Model", response.model)
        with col3:
            if response.tokens_used:
                st.metric("Tokens", response.tokens_used)

        # Display the analysis with formatting
        st.markdown("---")
        self._display_formatted_requirements(response.content)

        # Download options
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="📄 Download Table Analysis (TXT)",
                data=response.content,
                file_name=f"llm_table_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

        with col2:
            st.download_button(
                label="📝 Download Table Analysis (MD)",
                data=response.content,
                file_name=f"llm_table_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown"
            )

    def _render_visualizations_tab(self):
        """Render visualizations tab"""
        
        if not st.session_state.analysis_results:
            st.info("📈 Please complete the SQL analysis first to view visualizations.")
            return
        
        st.header("📈 Analysis Visualizations")
        
        results = st.session_state.analysis_results
        procedures = results['procedures']
        cross_analysis = results['cross_analysis']
        
        # Complexity distribution
        st.subheader("📊 Procedure Complexity Distribution")
        self._plot_complexity_distribution(procedures)
        
        # Table usage frequency
        st.subheader("📋 Table Usage Frequency")
        self._plot_table_usage(procedures)
        
        # Data lineage network
        st.subheader("🔗 Data Lineage Network")
        self._plot_data_lineage(cross_analysis.get('data_lineage', {}))
    
    def _plot_complexity_distribution(self, procedures: List[ProcedureAnalysis]):
        """Plot procedure complexity distribution"""
        
        complexity_scores = [p.complexity_score for p in procedures]
        procedure_names = [p.procedure_id for p in procedures]
        
        fig = px.bar(
            x=procedure_names,
            y=complexity_scores,
            title="Procedure Complexity Scores",
            labels={'x': 'Procedure', 'y': 'Complexity Score'}
        )
        fig.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
    
    def _plot_table_usage(self, procedures: List[ProcedureAnalysis]):
        """Plot table usage frequency"""
        
        table_counts = {}
        for proc in procedures:
            for table_name in proc.tables.keys():
                table_counts[table_name] = table_counts.get(table_name, 0) + 1
        
        if table_counts:
            # Sort by frequency
            sorted_tables = sorted(table_counts.items(), key=lambda x: x[1], reverse=True)
            tables, counts = zip(*sorted_tables[:20])  # Top 20
            
            fig = px.bar(
                x=list(tables),
                y=list(counts),
                title="Top 20 Most Used Tables",
                labels={'x': 'Table Name', 'y': 'Usage Count'}
            )
            fig.update_layout(xaxis_tickangle=45)
            st.plotly_chart(fig, use_container_width=True)
    
    def _plot_data_lineage(self, lineage_data: Dict[str, Any]):
        """Plot data lineage network"""
        
        if not lineage_data or not lineage_data.get('nodes'):
            st.info("No data lineage information available")
            return
        
        # Create network visualization using plotly
        nodes = lineage_data.get('nodes', [])
        edges = lineage_data.get('edges', [])
        
        if nodes:
            # Simple table relationship chart
            table_names = [node[0] for node in nodes]
            table_types = [node[1].get('table_type', 'Unknown') for node in nodes]
            
            fig = px.treemap(
                names=table_names,
                parents=[''] * len(table_names),
                values=[1] * len(table_names),
                title="Table Relationships Overview"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def _render_download_buttons(self):
        """Render download buttons in sidebar"""
        
        if not st.session_state.analysis_results:
            return
        
        # Create download package
        if st.sidebar.button("📦 Download All Results"):
            self._create_download_package()
    
    def _create_download_package(self):
        """Create a zip file with all analysis results"""
        
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            
            # Table analysis CSV
            if st.session_state.analysis_results:
                procedures = st.session_state.analysis_results['procedures']
                table_df = self._create_table_analysis_dataframe(procedures)
                if not table_df.empty:
                    csv_data = table_df.to_csv(index=False)
                    zip_file.writestr("table_analysis.csv", csv_data)
            
            # LLM requirements
            if st.session_state.llm_response and st.session_state.llm_response.success:
                zip_file.writestr("requirements.txt", st.session_state.llm_response.content)
            
            # Analysis summary JSON
            if st.session_state.analysis_results:
                # Convert to JSON-serializable format
                summary_data = {
                    'timestamp': st.session_state.analysis_results['timestamp'],
                    'summary': st.session_state.analysis_results['cross_analysis']['summary']
                }
                zip_file.writestr("analysis_summary.json", json.dumps(summary_data, indent=2))
        
        zip_buffer.seek(0)
        
        st.sidebar.download_button(
            label="📥 Download Package",
            data=zip_buffer.getvalue(),
            file_name=f"sap_hana_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
            mime="application/zip"
        )

def main():
    """Main application entry point"""
    app = SAP_HANA_Analyzer_App()
    app.run()

if __name__ == "__main__":
    main()
