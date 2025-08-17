#!/usr/bin/env python3
"""
Streamlit Chatbot Application Entry Point

This file serves as the main entry point for the Streamlit chatbot application.
It can be run directly or used as a module to start the application.

Usage:
    python app.py
    streamlit run app.py
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """
    Main function to run the Streamlit application.
    """
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Check if main.py exists
    main_py_path = script_dir / "main.py"
    if not main_py_path.exists():
        print("Error: main.py not found in the current directory.")
        print(f"Expected location: {main_py_path}")
        sys.exit(1)
    
    # Check if .env file exists
    env_path = script_dir / ".env"
    if not env_path.exists():
        print("Warning: .env file not found!")
        print("Please create a .env file with your API keys:")
        print("1. Copy .env-sample to .env")
        print("2. Add your Groq API key to the .env file")
        print("\nContinuing anyway...")
    
    # Run the Streamlit application
    try:
        print("🚀 Starting Streamlit Chatbot Application...")
        print("📱 The application will open in your browser at http://localhost:8501")
        print("⏹️  Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Run streamlit with main.py
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ], check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Streamlit: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Error: Streamlit not found!")
        print("Please install Streamlit: pip install streamlit")
        sys.exit(1)

if __name__ == "__main__":
    main()
