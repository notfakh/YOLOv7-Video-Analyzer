import os
import sys
import importlib.util
from argparse import Namespace
import cv2

# Add the YOLOv7 directory to the system path
yolov7_path = "C:\pythonProject\yolov7"
sys.path.append(yolov7_path)

# Dynamically load detect.py
detect_path = os.path.join(yolov7_path, "detect.py")
spec = importlib.util.spec_from_file_location("detect", detect_path)
detect_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(detect_module)

# Define video input and output paths
video_path = "vid.mp4"  # Path to input video
output_path = os.path.join(yolov7_path, "runs/detect")  # Output directory

# YOLOv7 configuration
opt = Namespace (
    weights=os.path.join(yolov7_path, "yolov7.pt"),  # Path to YOLOv7 weights
    source=video_path,  # Video file as input
    img_size=640,       # Inference image size
    conf_thres=0.25,    # Confidence threshold
    iou_thres=0.45,     # IoU threshold for NMS
    device='',          # Use GPU if available, otherwise CPU
    view_img=False,     # Display the results while processing
    save_txt=False,     # Skip saving detection results in a .txt file
    save_conf=False,    # Skip saving confidence scores
    nosave=False,       # Save output video with detections
    classes=None,       # Detect all classes
    agnostic_nms=False, # Class-agnostic NMS
    augment=False,      # No augmented inference
    update=False,       # Skip updating all models
    project=output_path, # Output directory
    name="video_results",  # Subdirectory for results
    exist_ok=True,       # Don't increment directory name if it exists
    no_trace=True        # Disable tracing
)

# Inject opt into the detect module
detect_module.opt = opt

# Run YOLOv7 detection on the video
print("Processing video for classification...")
detect_module.detect()  # Call the detect function
print("Video classification completed.")

# Check the output video path
output_video_path = os.path.join(output_path, opt.name, os.path.basename(video_path))
if os.path.exists(output_video_path):
    print(f"Classified video saved at: {output_video_path}")
else:
    print("Error: Output video not found.")
