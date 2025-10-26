#!/bin/bash

# Quick deployment script for Safety Object Detection App
# This script prepares your app for Streamlit Cloud deployment

echo "🛡️  Safety Object Detection - Quick Deploy Script"
echo "=================================================="
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
fi

# Run setup script
echo "🔧 Running setup script..."
python3 setup_streamlit_cloud.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps to deploy:"
echo ""
echo "1. Create a GitHub repository:"
echo "   - Go to github.com"
echo "   - Click 'New repository'"
echo "   - Give it a name (e.g., 'safety-object-detection')"
echo "   - Leave it empty (don't add README)"
echo ""
echo "2. Push your code to GitHub:"
echo "   git add ."
echo "   git commit -m 'Initial commit - Safety Object Detection App'"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Cloud:"
echo "   - Go to share.streamlit.io"
echo "   - Sign in with GitHub"
echo "   - Click 'New app'"
echo "   - Select your repository"
echo "   - Main file: app.py"
echo "   - Click 'Deploy'"
echo ""
echo "🎉 Your app will be live in 2-3 minutes!"
echo ""
echo "📚 For more details, see DEPLOYMENT_GUIDE.md"

