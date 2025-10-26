#!/bin/bash
# Script to run the Safety Object Detection web app

cd "$(dirname "$0")"
echo "Starting Safety Object Detection App..."
echo ""
echo "The app will open in your browser at: http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py

