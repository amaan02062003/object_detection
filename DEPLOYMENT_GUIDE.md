# Deploying Your Safety Object Detection App Online

## Option 1: Streamlit Cloud (Recommended - FREE & EASIEST)

### Prerequisites:
1. GitHub account (free at github.com)
2. Your project on GitHub

### Steps:

1. **Create a GitHub Repository**
   ```bash
   cd /Users/mohammadansari/Desktop/Hackathon/Hackathon2_scripts
   git init
   git add .
   git commit -m "Initial commit - Safety Object Detection App"
   ```

2. **Create GitHub repo and push**:
   - Go to github.com and create a new repository
   - Follow the instructions to push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Main file path: `app.py`
   - Click "Deploy"
   - Your app will be live in 2-3 minutes!

### Your app will be at: `https://YOUR-APP-NAME.streamlit.app`

---

## Option 2: Streamlit Community Cloud (Even Easier)

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "Get Started"
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Your app auto-deploys!

---

## Option 3: Heroku Deployment

### Setup:

1. **Install Heroku CLI** (if not installed)
2. **Create Procfile**:
   ```
   echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

3. **Deploy**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

---

## Option 4: AWS/Docker (Advanced)

See the `Dockerfile` in this directory for containerized deployment.

---

## What Gets Deployed

- ✅ Your trained YOLO model
- ✅ Streamlit web interface
- ✅ All detection capabilities
- ✅ Real-time image upload and processing

## Important Files for Deployment

- `app.py` - Main application
- `yolo_params.yaml` - Model configuration
- `runs/detect/train*/weights/best.pt` - Model weights
- `requirements.txt` - Python dependencies
- `packages.txt` (if needed for system dependencies)

## Model Size Note

Your model file (`best.pt`) is ~64MB. Make sure to:
1. Keep it in the repository
2. Use Git LFS if the repo gets large

```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes
git add runs/detect/train2/weights/best.pt
git commit -m "Add model with LFS"
```

## Troubleshooting

### If deployment fails:
1. Check `requirements.txt` is complete
2. Ensure model path is correct
3. Verify all dependencies are listed

### Updating the deployed app:
Just push new commits to GitHub - Streamlit Cloud auto-updates!

---

**Recommended: Use Streamlit Cloud for easiest deployment!** 🚀

