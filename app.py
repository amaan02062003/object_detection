import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path
import os
from PIL import Image
import io
import torch

# Page configuration
st.set_page_config(
    page_title="Safety Object Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 2rem;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #1565c0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'model' not in st.session_state:
    st.session_state.model = None
    st.session_state.model_loaded = False

@st.cache_resource
def load_model():
    """Load the YOLO model from the latest training run"""
    try:
        this_dir = Path(__file__).parent
        detect_path = this_dir / "runs" / "detect"
        train_folders = sorted([f for f in os.listdir(detect_path) 
                               if os.path.isdir(detect_path / f) and f.startswith("train")])
        
        if len(train_folders) == 0:
            st.error("No training folders found. Please train a model first.")
            return None
        
        model_path = detect_path / train_folders[-1] / "weights" / "best.pt"
        
        if not model_path.exists():
            st.error(f"Model file not found at {model_path}")
            return None
        
        model = YOLO(model_path)
        return model, train_folders[-1]
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def main():
    # Header
    st.markdown('<p class="main-header">🛡️ Safety Object Detection</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Detect safety equipment in images using AI</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Model Information")
        
        # Load model with progress indicator
        if not st.session_state.model_loaded:
            with st.spinner("Loading model..."):
                model_data = load_model()
                if model_data:
                    st.session_state.model, model_name = model_data
                    st.session_state.model_loaded = True
                    st.success(f"✅ Model loaded: {model_name}")
                else:
                    st.error("❌ Failed to load model")
        
        if st.session_state.model_loaded:
            st.markdown("---")
            st.subheader("🎯 Detected Classes")
            class_names = ['OxygenTank', 'NitrogenTank', 'FirstAidBox', 
                          'FireAlarm', 'SafetySwitchPanel', 'EmergencyPhone', 'FireExtinguisher']
            
            for i, name in enumerate(class_names):
                emoji = ['🔵', '🔷', '➕', '🔥', '⚙️', '📞', '🧯'][i]
                st.markdown(f"{emoji} {name}")
            
            st.markdown("---")
            st.subheader("ℹ️ Instructions")
            st.markdown("""
            1. Upload an image using the file uploader
            2. Click 'Detect Safety Objects'
            3. View the detected objects with bounding boxes
            """)
    
    # Main content area
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=['png', 'jpg', 'jpeg'],
            help="Upload an image to detect safety objects"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width="stretch")
    
    with col2:
        st.subheader("🔍 Detection Results")
        
        if uploaded_file is None:
            st.info("👆 Please upload an image to get started")
        else:
            # Detection button
            detect_button = st.button("🚀 Detect Safety Objects", type="primary")
            
            if detect_button and st.session_state.model is not None:
                with st.spinner("Analyzing image..."):
                    # Perform detection
                    image_np = np.array(image)
                    results = st.session_state.model.predict(image_np, conf=0.5, imgsz=640)
                    
                    # Get the first result
                    result = results[0]
                    
                    # Draw bounding boxes
                    annotated_image = result.plot()
                    annotated_pil = Image.fromarray(annotated_image)
                    
                    # Display annotated image
                    st.image(annotated_pil, caption="Detected Objects", width="stretch")
                    
                    # Show detection statistics
                    st.markdown("---")
                    st.subheader("📈 Detection Statistics")
                    
                    # Count detections for each class
                    class_counts = {}
                    confidence_scores = {}
                    
                    class_names = ['OxygenTank', 'NitrogenTank', 'FirstAidBox', 
                                  'FireAlarm', 'SafetySwitchPanel', 'EmergencyPhone', 'FireExtinguisher']
                    
                    for box in result.boxes:
                        class_id = int(box.cls[0])
                        conf = float(box.conf[0])
                        class_name = class_names[class_id]
                        
                        if class_name not in class_counts:
                            class_counts[class_name] = 0
                            confidence_scores[class_name] = []
                        
                        class_counts[class_name] += 1
                        confidence_scores[class_name].append(conf)
                    
                    # Display metrics
                    if class_counts:
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("Total Objects Detected", sum(class_counts.values()))
                        with col_b:
                            st.metric("Unique Classes", len(class_counts))
                        with col_c:
                            avg_conf = np.mean([np.mean(confidence_scores[cls]) for cls in confidence_scores])
                            st.metric("Avg Confidence", f"{avg_conf:.2%}")
                        
                        # Detailed breakdown
                        st.markdown("---")
                        st.subheader("🔬 Detailed Breakdown")
                        
                        for class_name in sorted(class_counts.keys()):
                            count = class_counts[class_name]
                            avg_conf = np.mean(confidence_scores[class_name])
                            max_conf = max(confidence_scores[class_name])
                            
                            col_x, col_y, col_z = st.columns(3)
                            with col_x:
                                st.markdown(f"**{class_name}**")
                            with col_y:
                                st.metric("Count", count)
                            with col_z:
                                st.metric("Avg Confidence", f"{avg_conf:.2%}")
                    else:
                        st.warning("⚠️ No objects detected in this image")
                    
                    # Show bounding box details
                    if result.boxes is not None and len(result.boxes) > 0:
                        st.markdown("---")
                        st.subheader("📍 Bounding Box Details")
                        
                        with st.expander("View all detections"):
                            for i, box in enumerate(result.boxes):
                                class_id = int(box.cls[0])
                                class_name = class_names[class_id]
                                conf = float(box.conf[0])
                                x1, y1, x2, y2 = box.xyxy[0].tolist()
                                width = x2 - x1
                                height = y2 - y1
                                
                                st.markdown(f"""
                                **Detection #{i+1}:**
                                - Class: {class_name}
                                - Confidence: {conf:.2%}
                                - Position: ({int(x1)}, {int(y1)})
                                - Size: {int(width)} x {int(height)} px
                                """)
            elif detect_button:
                st.error("⚠️ Model not loaded. Please check the sidebar.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>Safety Object Detection System | Built with YOLOv8 and Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

