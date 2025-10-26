# Quick Start Guide - Safety Object Detection App

## 🚀 The App is Running!

Your Streamlit application is currently running on:
**http://localhost:8501**

## 📋 How to Access

1. Open your web browser
2. Navigate to: http://localhost:8501
3. You'll see the Safety Object Detection interface

## 🎯 How to Use

1. **Upload an Image**
   - Click on "Choose an image..." in the upload section
   - Select a PNG, JPG, or JPEG image from your computer
   - The image will appear in the left panel

2. **Run Detection**
   - Click the "🚀 Detect Safety Objects" button
   - Wait a few seconds for the AI to analyze the image
   - Results will appear in the right panel

3. **View Results**
   - See the annotated image with colored bounding boxes
   - Check statistics (total objects, unique classes, confidence)
   - See detailed breakdown for each detected object class
   - Expand "Bounding Box Details" for coordinate information

## 🛡️ Detected Safety Objects

The system detects these 7 safety equipment types:
- 🔵 Oxygen Tank
- 🔷 Nitrogen Tank  
- ➕ First Aid Box
- 🔥 Fire Alarm
- ⚙️ Safety Switch Panel
- 📞 Emergency Phone
- 🧯 Fire Extinguisher

## ⚙️ Stop the Server

To stop the running server, press `Ctrl+C` in the terminal where it's running, or run:

```bash
pkill -f "streamlit run app.py"
```

## 🔄 Restart the App

To restart the application later:

```bash
cd Hackathon2_scripts
streamlit run app.py
```

Or use the provided script:

```bash
./run_app.sh
```

## 💡 Tips

- Try different lighting conditions (light, dark) to test robustness
- Test with cluttered and uncluttered images
- The model works best with clear, well-lit images
- Use images that contain safety equipment for best results

## 📊 Model Performance

Your trained model achieves:
- **mAP50**: 0.575 (overall)
- **Best Class**: Oxygen Tank (0.741 mAP50)
- **Average Inference Speed**: ~100ms per image

Enjoy detecting safety objects! 🎉

