# Safety Object Detection System

A web-based application for detecting safety equipment in images using YOLO object detection.

## Features

- 🛡️ **Safety Object Detection**: Detect 7 different types of safety equipment
- 📤 **Image Upload**: Easy image upload interface
- 🎨 **Beautiful UI**: Modern and aesthetic user interface
- 📊 **Detailed Statistics**: View detection statistics and confidence scores
- 🔍 **Bounding Box Visualization**: Visual display of detected objects

## Detected Objects

- 🔵 Oxygen Tank
- 🔷 Nitrogen Tank
- ➕ First Aid Box
- 🔥 Fire Alarm
- ⚙️ Safety Switch Panel
- 📞 Emergency Phone
- 🧯 Fire Extinguisher

## Installation

1. Install required packages:
```bash
pip install streamlit ultralytics opencv-python pillow numpy
```

## Running the Application

1. Navigate to the Hackathon2_scripts directory:
```bash
cd Hackathon2_scripts
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The app will automatically open in your browser at `http://localhost:8501`

## Usage

1. **Upload an Image**: Click the file uploader and select an image (PNG, JPG, or JPEG)
2. **Click "Detect Safety Objects"**: The AI will analyze the image
3. **View Results**: 
   - See the annotated image with bounding boxes
   - Check detection statistics
   - View detailed breakdown by class
   - See bounding box coordinates

## Project Structure

```
Hackathon2_scripts/
├── app.py                  # Streamlit web application
├── predict.py              # Batch prediction script
├── train.py                # Training script
├── yolo_params.yaml        # Model configuration
├── runs/detect/            # Training runs and model weights
│   └── train2/
│       └── weights/
│           └── best.pt     # Best model weights
└── predictions/            # Batch prediction results
    ├── images/             # Annotated images
    └── labels/             # Bounding box labels
```

## Model Information

- **Architecture**: YOLOv8
- **Input Size**: 640x640
- **Classes**: 7 safety equipment types
- **Confidence Threshold**: 0.5

## Notes

- The app automatically loads the latest trained model
- Make sure you have trained a model before using the app
- The model weights should be in `runs/detect/train*/weights/best.pt`

## Development

This application uses:
- **Streamlit**: For the web interface
- **Ultralytics YOLO**: For object detection
- **OpenCV**: For image processing
- **Pillow**: For image handling

## Troubleshooting

**Model not found error**:
- Ensure you have trained a model using `train.py`
- Check that the weights file exists in `runs/detect/train*/weights/best.pt`

**App won't start**:
- Make sure all dependencies are installed
- Check that port 8501 is not already in use

