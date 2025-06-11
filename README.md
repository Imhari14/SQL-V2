# SAP HANA SQL Analyzer - Streamlit Web Application

A comprehensive web application for analyzing SAP HANA SQL procedures and generating migration requirements documentation using advanced LLMs.

## 🎯 Features

### Core Functionality
- **Multi-file Upload**: Upload up to 100 SQL procedure files
- **Advanced SQL Parsing**: Sophisticated analysis of SAP HANA procedures
- **Cross-Procedure Analysis**: Identify patterns across all procedures
- **Migration Insights**: Specialized analysis for data migration planning

### LLM Integration
- **Dual LLM Support**: Azure OpenAI GPT-4 and Google Gemini
- **Robust Error Handling**: Automatic fallback between providers
- **Custom Prompts**: Option to use custom prompts for requirements generation
- **Streaming Responses**: Real-time response generation

### Output Formats
- **Table-by-Table Analysis**: Exact format requested (one row per table)
- **CSV Downloads**: Ready for Excel and documentation tools
- **Text Reports**: Comprehensive requirements documentation
- **Interactive Visualizations**: Charts and graphs for analysis insights

### Migration-Specific Features
- **Filter Pattern Analysis**: Identifies where filters can be optimized
- **Join Relationship Mapping**: Complex join analysis for migration planning
- **Data Lineage Visualization**: Understanding data flow and dependencies
- **Critical Point Identification**: Highlights migration risks and priorities

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Internet connection for LLM APIs

### Installation & Setup

1. **Navigate to the application directory:**
   ```bash
   cd streamlit_app
   ```

2. **Run the setup script:**
   ```bash
   python run.py --setup-only
   ```

3. **Configure API keys:**
   Edit the `.env` file with your API keys:
   ```env
   # Azure OpenAI Configuration
   AZURE_OPENAI_API_KEY=your_azure_api_key_here
   
   # Google Gemini Configuration  
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Install dependencies and run:**
   ```bash
   python run.py
   ```

5. **Open your browser:**
   Navigate to `http://localhost:8501`

### Alternative Quick Start
```bash
# Install dependencies only
python run.py --install-only

# Run on different port/host
python run.py --port 8080 --host 0.0.0.0
```

## 📋 Usage Guide

### 1. Upload SQL Procedures

**Option A: File Upload**
- Click "Upload Files" 
- Select multiple `.sql`, `.hdbprocedure`, or `.txt` files
- Up to 100 procedures supported

**Option B: Paste SQL Text**
- Click "Paste SQL Text"
- Enter procedure name and SQL content
- Good for single procedure analysis

### 2. Configure Analysis

**LLM Provider Selection:**
- Choose between Azure OpenAI or Google Gemini
- Test connection before analysis
- Automatic fallback if primary provider fails

**Analysis Settings:**
- Set maximum procedures to analyze
- Configure batch processing options

### 3. Run Analysis

- Click "🚀 Start Analysis"
- Monitor real-time progress
- View quick summary upon completion

### 4. Review Results

**Table-by-Table Analysis:**
- One row per table (your exact requested format)
- All columns, filters, joins for each table
- Download as CSV for Excel integration

**Filter Pattern Analysis:**
- Identifies filter optimization opportunities
- Shows where procedures need all values vs. filtered values
- Migration-specific recommendations

**Join Relationship Analysis:**
- Complex join patterns across procedures
- Performance optimization suggestions
- Data integrity validation requirements

### 5. Generate Requirements

**LLM-Powered Documentation:**
- Comprehensive migration requirements
- Technical implementation guide
- Risk assessment and mitigation strategies
- Success criteria and validation checkpoints

**Custom Prompts:**
- Option to use custom prompts
- Tailored for specific migration needs
- Professional documentation output

### 6. Download Results

**Individual Downloads:**
- Table analysis (CSV)
- Requirements documentation (TXT)
- Analysis summary (JSON)

**Complete Package:**
- ZIP file with all results
- Ready for team sharing
- Timestamped for version control

## 🔧 Configuration

### Environment Variables

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://models.inference.ai.azure.com
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_MODEL=gpt-4o

# Google Gemini Configuration
GEMINI_API_KEY=your_gemini_api_key

# App Configuration
DEFAULT_LLM_PROVIDER=azure
MAX_PROCEDURES=100
ANALYSIS_TIMEOUT=300
```

### API Key Setup

**Azure OpenAI:**
1. Get API key from Azure OpenAI service
2. Update `AZURE_OPENAI_API_KEY` in `.env`
3. Verify endpoint URL matches your deployment

**Google Gemini:**
1. Get API key from Google AI Studio
2. Update `GEMINI_API_KEY` in `.env`
3. Ensure Gemini API access is enabled

## 📊 Output Format

### Table Analysis (CSV)
```
Procedure ID | Table Name | Column Name | Used As | Filter Condition | Join Condition | Notes
PR_001 | VBAK | VBAK.VBELN, VBAK.VBTYP | SELECT, JOIN | VBAK.VBTYP = 'C' | VBAK.VBELN = VBAP.VBELN | Sales document header
```

### Requirements Documentation
- Executive Summary
- Data Migration Strategy  
- Join Relationship Requirements
- Filter Logic Optimization
- Technical Implementation Guide
- Risk Assessment and Mitigation
- Success Criteria and Validation

## 🎯 Migration-Specific Features

### Filter Analysis
- **Cross-Procedure Patterns**: Identifies where 4 out of 5 procedures filter a column for specific values, while the 5th needs all values
- **Optimization Recommendations**: Suggests where filters can be consolidated or removed for migration
- **Parameter Standardization**: Identifies opportunities for parameter reuse

### Join Analysis  
- **Complex Join Patterns**: Analyzes multi-level joins across procedures
- **Performance Impact**: Identifies joins that may impact migration performance
- **Data Integrity**: Ensures join relationships are maintained in new system

### Data Lineage
- **Dependency Mapping**: Shows how data flows between tables
- **Migration Sequence**: Recommends order for table migration
- **Critical Path Analysis**: Identifies tables that must be migrated first

## 🛠️ Troubleshooting

### Common Issues

**1. API Connection Failures**
- Verify API keys are correct
- Check internet connectivity
- Test connection using sidebar button

**2. Large File Processing**
- Reduce number of procedures if timeout occurs
- Use batch processing for 50+ procedures
- Monitor memory usage for very large files

**3. Parsing Errors**
- Ensure SQL syntax is valid SAP HANA SQL
- Check for unsupported SQL constructs
- Review error messages in application

### Performance Tips

**For 50+ Procedures:**
- Use Azure OpenAI for better throughput
- Process in batches of 10-20 procedures
- Allow extra time for cross-procedure analysis

**For Complex Procedures:**
- Monitor complexity scores in results
- Focus on high-complexity procedures first
- Use custom prompts for specific requirements

## 📁 File Structure

```
streamlit_app/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration settings
├── sql_parser.py         # Advanced SQL parsing engine
├── llm_service.py        # LLM integration service
├── run.py                # Application runner script
├── requirements.txt      # Python dependencies
├── .env.example         # Environment template
├── .env                 # Your environment variables
└── README.md            # This documentation
```

## 🎉 Ready for Your Team

This application is designed for easy presentation to your teammates:

1. **Professional Interface**: Clean, intuitive web interface
2. **Comprehensive Analysis**: Covers all migration requirements
3. **Multiple Output Formats**: CSV, TXT, JSON, and visualizations
4. **Robust LLM Integration**: Dual provider support with fallback
5. **Migration-Focused**: Specifically designed for data migration projects

## 🚀 Deployment Options

**Local Development:**
```bash
python run.py
```

**Team Sharing:**
```bash
python run.py --host 0.0.0.0 --port 8080
```

**Production Deployment:**
- Deploy to Streamlit Cloud
- Use Docker containerization
- Deploy to cloud platforms (AWS, Azure, GCP)

---

**Ready to analyze your 50+ SAP HANA procedures and generate comprehensive migration requirements!** 🎯
