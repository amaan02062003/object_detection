#!/usr/bin/env python3
"""
Setup script for Streamlit Cloud deployment
This ensures the model paths and environment are configured correctly
"""

import os
import shutil
from pathlib import Path

def setup_for_deployment():
    """Prepare the app for Streamlit Cloud deployment"""
    
    print("🚀 Setting up for Streamlit Cloud deployment...")
    
    # Get current directory
    base_dir = Path(__file__).parent
    
    # Check if model exists
    runs_dir = base_dir / "runs" / "detect"
    
    if not runs_dir.exists():
        print("❌ Error: No model found. Please train a model first.")
        return False
    
    # Find the latest training folder
    train_folders = sorted([f for f in os.listdir(runs_dir) 
                           if os.path.isdir(runs_dir / f) and f.startswith("train")])
    
    if not train_folders:
        print("❌ Error: No training folders found.")
        return False
    
    latest_model = runs_dir / train_folders[-1] / "weights" / "best.pt"
    
    if not latest_model.exists():
        print("❌ Error: Model weights not found at", latest_model)
        return False
    
    print(f"✅ Found model: {latest_model}")
    
    # Create .streamlit directory if it doesn't exist
    streamlit_dir = base_dir / ".streamlit"
    streamlit_dir.mkdir(exist_ok=True)
    
    # Create config.toml if it doesn't exist
    config_file = streamlit_dir / "config.toml"
    if not config_file.exists():
        config_content = """[server]
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
"""
        config_file.write_text(config_content)
        print("✅ Created .streamlit/config.toml")
    
    print("\n✅ Setup complete!")
    print("\nNext steps:")
    print("1. Initialize git: git init")
    print("2. Add all files: git add .")
    print("3. Commit: git commit -m 'Deploy Safety Object Detection App'")
    print("4. Create GitHub repo and push")
    print("5. Deploy on share.streamlit.io")
    print("\n📖 See DEPLOYMENT_GUIDE.md for detailed instructions")
    
    return True

if __name__ == "__main__":
    setup_for_deployment()

