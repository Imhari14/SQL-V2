#!/usr/bin/env python3
"""
SAP HANA SQL Analyzer - Deployment Script
=========================================

This script provides comprehensive deployment options for the Streamlit application
including local development, team sharing, and production deployment.
"""

import os
import sys
import subprocess
import shutil
import json
from pathlib import Path
from datetime import datetime

class DeploymentManager:
    """Manages deployment of the SAP HANA SQL Analyzer application"""
    
    def __init__(self):
        self.app_dir = Path(__file__).parent
        self.project_name = "sap-hana-sql-analyzer"
        
    def check_environment(self):
        """Check deployment environment"""
        print("🔍 Checking deployment environment...")
        
        issues = []
        
        # Check Python version
        if sys.version_info < (3, 8):
            issues.append("Python 3.8+ required")
        
        # Check required files
        required_files = [
            'app.py', 'config.py', 'sql_parser.py', 
            'llm_service.py', 'requirements.txt'
        ]
        
        for file in required_files:
            if not (self.app_dir / file).exists():
                issues.append(f"Missing required file: {file}")
        
        # Check environment file
        if not (self.app_dir / '.env').exists():
            if (self.app_dir / '.env.example').exists():
                print("📝 Creating .env from template...")
                shutil.copy(self.app_dir / '.env.example', self.app_dir / '.env')
                print("✅ .env file created. Please update with your API keys.")
            else:
                issues.append("No .env or .env.example file found")
        
        if issues:
            print("❌ Environment issues found:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        
        print("✅ Environment check passed")
        return True
    
    def install_dependencies(self):
        """Install Python dependencies"""
        print("📦 Installing dependencies...")
        
        try:
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', '-r', 
                str(self.app_dir / 'requirements.txt')
            ], check=True, cwd=self.app_dir)
            
            print("✅ Dependencies installed successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            return False
    
    def run_local_development(self, port=8501, host='localhost'):
        """Run local development server"""
        print(f"🚀 Starting local development server on {host}:{port}")
        
        try:
            cmd = [
                sys.executable, '-m', 'streamlit', 'run', 'app.py',
                '--server.port', str(port),
                '--server.address', host,
                '--server.headless', 'true',
                '--browser.gatherUsageStats', 'false',
                '--theme.base', 'light'
            ]
            
            print(f"📱 Open your browser to: http://{host}:{port}")
            print("⏹️  Press Ctrl+C to stop the server")
            
            subprocess.run(cmd, cwd=self.app_dir)
            
        except KeyboardInterrupt:
            print("\n👋 Development server stopped")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to start development server: {e}")
    
    def run_team_server(self, port=8080):
        """Run server accessible to team members"""
        print(f"👥 Starting team server on all interfaces, port {port}")
        
        try:
            cmd = [
                sys.executable, '-m', 'streamlit', 'run', 'app.py',
                '--server.port', str(port),
                '--server.address', '0.0.0.0',
                '--server.headless', 'true',
                '--browser.gatherUsageStats', 'false'
            ]
            
            # Get local IP for team access
            import socket
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            
            print(f"📱 Team access URLs:")
            print(f"   Local: http://localhost:{port}")
            print(f"   Network: http://{local_ip}:{port}")
            print("⏹️  Press Ctrl+C to stop the server")
            
            subprocess.run(cmd, cwd=self.app_dir)
            
        except KeyboardInterrupt:
            print("\n👋 Team server stopped")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to start team server: {e}")
    
    def create_docker_deployment(self):
        """Create Docker deployment files"""
        print("🐳 Creating Docker deployment...")
        
        # Create Dockerfile
        dockerfile_content = '''FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    curl \\
    software-properties-common \\
    git \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
'''
        
        # Create docker-compose.yml
        docker_compose_content = '''version: '3.8'

services:
  sap-hana-analyzer:
    build: .
    ports:
      - "8501:8501"
    environment:
      - AZURE_OPENAI_API_KEY=${AZURE_OPENAI_API_KEY}
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
'''
        
        # Create .dockerignore
        dockerignore_content = '''__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git
.mypy_cache
.pytest_cache
.hypothesis
.DS_Store
.env
'''
        
        # Write files
        (self.app_dir / 'Dockerfile').write_text(dockerfile_content)
        (self.app_dir / 'docker-compose.yml').write_text(docker_compose_content)
        (self.app_dir / '.dockerignore').write_text(dockerignore_content)
        
        print("✅ Docker files created:")
        print("  - Dockerfile")
        print("  - docker-compose.yml") 
        print("  - .dockerignore")
        print("\n🚀 To deploy with Docker:")
        print("  docker-compose up --build")
    
    def create_streamlit_cloud_config(self):
        """Create Streamlit Cloud deployment configuration"""
        print("☁️ Creating Streamlit Cloud configuration...")
        
        # Create .streamlit/config.toml
        streamlit_dir = self.app_dir / '.streamlit'
        streamlit_dir.mkdir(exist_ok=True)
        
        config_content = '''[global]
developmentMode = false

[server]
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
base = "light"
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
'''
        
        (streamlit_dir / 'config.toml').write_text(config_content)
        
        # Create secrets template
        secrets_content = '''# Streamlit Cloud Secrets
# Add these in your Streamlit Cloud app settings

AZURE_OPENAI_API_KEY = "your_azure_openai_api_key"
AZURE_OPENAI_ENDPOINT = "https://models.inference.ai.azure.com"
AZURE_OPENAI_MODEL = "gpt-4o"

GEMINI_API_KEY = "your_gemini_api_key"

DEFAULT_LLM_PROVIDER = "azure"
MAX_PROCEDURES = 100
'''
        
        (streamlit_dir / 'secrets.toml.example').write_text(secrets_content)
        
        print("✅ Streamlit Cloud files created:")
        print("  - .streamlit/config.toml")
        print("  - .streamlit/secrets.toml.example")
        print("\n☁️ To deploy to Streamlit Cloud:")
        print("  1. Push code to GitHub")
        print("  2. Connect repository in Streamlit Cloud")
        print("  3. Add secrets from secrets.toml.example")
    
    def run_tests(self):
        """Run application tests"""
        print("🧪 Running application tests...")
        
        try:
            # Test imports
            print("Testing imports...")
            test_script = '''
import sys
sys.path.append(".")

try:
    from config import Config
    from sql_parser import AdvancedSQLParser
    from llm_service import LLMService
    import app
    print("✅ All imports successful")
except Exception as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)

# Test configuration
try:
    config = Config()
    issues = config.validate_config()
    if issues:
        print("⚠️ Configuration issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ Configuration valid")
except Exception as e:
    print(f"❌ Configuration error: {e}")

# Test SQL parser
try:
    parser = AdvancedSQLParser()
    print("✅ SQL parser initialized")
except Exception as e:
    print(f"❌ SQL parser error: {e}")

# Test LLM service
try:
    llm_service = LLMService()
    print("✅ LLM service initialized")
except Exception as e:
    print(f"❌ LLM service error: {e}")

print("🎉 All tests passed!")
'''
            
            result = subprocess.run([
                sys.executable, '-c', test_script
            ], cwd=self.app_dir, capture_output=True, text=True)
            
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
            
            return result.returncode == 0
            
        except Exception as e:
            print(f"❌ Test execution failed: {e}")
            return False
    
    def create_deployment_package(self):
        """Create deployment package"""
        print("📦 Creating deployment package...")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        package_name = f"{self.project_name}_{timestamp}"
        package_dir = self.app_dir.parent / package_name
        
        # Create package directory
        package_dir.mkdir(exist_ok=True)
        
        # Copy application files
        files_to_copy = [
            'app.py', 'config.py', 'sql_parser.py', 'llm_service.py',
            'requirements.txt', 'README.md', 'run.py', 'deploy.py'
        ]
        
        for file in files_to_copy:
            src = self.app_dir / file
            if src.exists():
                shutil.copy2(src, package_dir / file)
        
        # Copy directories
        dirs_to_copy = ['sample_procedures', '.streamlit']
        for dir_name in dirs_to_copy:
            src_dir = self.app_dir / dir_name
            if src_dir.exists():
                shutil.copytree(src_dir, package_dir / dir_name, dirs_exist_ok=True)
        
        # Copy environment template
        env_example = self.app_dir / '.env.example'
        if env_example.exists():
            shutil.copy2(env_example, package_dir / '.env.example')
        
        # Create deployment instructions
        instructions = f'''# SAP HANA SQL Analyzer - Deployment Package

Generated: {datetime.now().isoformat()}

## Quick Start

1. Configure environment:
   cp .env.example .env
   # Edit .env with your API keys

2. Install and run:
   python run.py

## Deployment Options

- Local development: python run.py
- Team sharing: python deploy.py --team
- Docker: docker-compose up --build
- Streamlit Cloud: Push to GitHub and connect

## Files Included

{chr(10).join(f"- {f}" for f in files_to_copy)}

## Support

For issues or questions, refer to README.md
'''
        
        (package_dir / 'DEPLOYMENT.md').write_text(instructions)
        
        print(f"✅ Deployment package created: {package_dir}")
        return package_dir

def main():
    """Main deployment function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='SAP HANA SQL Analyzer Deployment')
    parser.add_argument('--check', action='store_true', help='Check environment only')
    parser.add_argument('--install', action='store_true', help='Install dependencies only')
    parser.add_argument('--dev', action='store_true', help='Run development server')
    parser.add_argument('--team', action='store_true', help='Run team server')
    parser.add_argument('--docker', action='store_true', help='Create Docker files')
    parser.add_argument('--cloud', action='store_true', help='Create Streamlit Cloud config')
    parser.add_argument('--test', action='store_true', help='Run tests')
    parser.add_argument('--package', action='store_true', help='Create deployment package')
    parser.add_argument('--port', type=int, default=8501, help='Port number')
    
    args = parser.parse_args()
    
    deployer = DeploymentManager()
    
    print("🚀 SAP HANA SQL Analyzer - Deployment Manager")
    print("=" * 50)
    
    # Check environment
    if not deployer.check_environment():
        sys.exit(1)
    
    if args.check:
        print("✅ Environment check complete")
        return
    
    # Install dependencies
    if args.install or args.dev or args.team:
        if not deployer.install_dependencies():
            sys.exit(1)
    
    if args.install:
        print("✅ Dependencies installation complete")
        return
    
    # Run tests
    if args.test:
        if not deployer.run_tests():
            sys.exit(1)
        return
    
    # Create Docker files
    if args.docker:
        deployer.create_docker_deployment()
        return
    
    # Create Streamlit Cloud config
    if args.cloud:
        deployer.create_streamlit_cloud_config()
        return
    
    # Create deployment package
    if args.package:
        deployer.create_deployment_package()
        return
    
    # Run servers
    if args.team:
        deployer.run_team_server(args.port)
    elif args.dev:
        deployer.run_local_development(args.port)
    else:
        # Default: run development server
        deployer.run_local_development(args.port)

if __name__ == "__main__":
    main()
