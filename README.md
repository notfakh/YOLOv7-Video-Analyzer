# YOLOv7-Video-Analyzer
Processes a video using YOLOv7 by dynamically loading the detection module, applying object detection frame-by-frame, and saving the annotated output video automatically.

## 📋 Project Overview

This project provides a Python wrapper for running YOLOv7 object detection on video files. It processes each frame, detects objects, draws bounding boxes, and outputs an annotated video with all detections visualized.

## 🎯 What Does This Do?

- **Processes** video files frame-by-frame
- **Detects** 80 object classes (COCO dataset) in real-time
- **Draws** bounding boxes with class labels and confidence scores
- **Outputs** annotated video file with all detections
- **Supports** various video formats (MP4, AVI, MOV, etc.)
- **Utilizes** GPU acceleration for faster processing
- **Maintains** original video resolution and frame rate

## 🔑 Key Features

- ✅ Video object detection with YOLOv7
- ✅ Real-time frame-by-frame processing
- ✅ Automatic output video generation
- ✅ Configurable detection parameters
- ✅ GPU/CPU support
- ✅ Multiple video format support
- ✅ Non-Maximum Suppression (NMS)
- ✅ Progress tracking during processing

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
CUDA (optional, for GPU acceleration - highly recommended for videos)
FFmpeg (for video codec support)
```

### Installation

1. Clone YOLOv7 repository:
```bash
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt
```

2. Download YOLOv7 weights:
```bash
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```

3. Clone this wrapper repository:
```bash
git clone https://github.com/notfakh/yolov7-video-detection.git
cd yolov7-video-detection
```

4. Install additional requirements:
```bash
pip install -r requirements.txt
```

### Project Structure

```
project/
│
├── yolov7/                          # YOLOv7 official repository
│   ├── detect.py
│   ├── yolov7.pt                   # Pre-trained weights
│   └── runs/detect/video_results/  # Output directory
│
├── yolov7_video_detector.py        # This wrapper script
├── your_video.mp4                  # Input video
└── requirements.txt
```

### Usage

1. Update paths in the script:
```python
yolov7_path = "path/to/yolov7"           # YOLOv7 directory
video_path = "path/to/your_video.mp4"    # Input video
```

2. Run detection:
```bash
python yolov7_video_detector.py
```

**Output:**
```
Processing video for classification...
video 1/1 (frame 1/300) /path/to/video.mp4: 640x480 2 persons, 1 car, Done. (0.023s)
video 1/1 (frame 2/300) /path/to/video.mp4: 640x480 3 persons, 1 car, Done. (0.021s)
...
Video classification completed.
Classified video saved at: C:/pythonProject/yolov7/runs/detect/video_results/your_video.mp4
```

## 📊 Detection Parameters

### Core Configuration:

```python
opt = Namespace(
    weights="yolov7.pt",     # Model weights
    source="video.mp4",      # Input video file
    img_size=640,            # Inference size (pixels)
    conf_thres=0.25,         # Confidence threshold (0.0-1.0)
    iou_thres=0.45,          # IoU threshold for NMS
    device='',               # '' = auto, '0' = GPU, 'cpu' = CPU
    view_img=False,          # Display during processing
    save_txt=False,          # Don't save text labels
    nosave=False,            # Save output video
    classes=None,            # Filter by class (None = all)
)
```

### Parameter Tuning Guide:

| Parameter | Low Value | High Value | Effect |
|-----------|-----------|------------|--------|
| **conf_thres** | 0.15 | 0.5 | Low = More detections, High = Fewer, more confident |
| **iou_thres** | 0.3 | 0.6 | Low = Fewer overlaps, High = More overlaps allowed |
| **img_size** | 416 | 1280 | Low = Faster, High = More accurate |

## 🎬 Video Processing Workflow

### Step-by-Step Process:

1. **Load Video**
   - Reads video file
   - Extracts frame rate and resolution
   - Prepares for frame-by-frame processing

2. **Process Each Frame**
   - Resizes frame to inference size (640x640)
   - Runs YOLOv7 detection
   - Applies Non-Maximum Suppression
   - Draws bounding boxes and labels

3. **Save Output Video**
   - Combines processed frames
   - Maintains original frame rate
   - Saves with same codec as input

4. **Complete**
   - Reports processing time
   - Shows output path
   - Displays detection statistics

## 🎨 Detected Object Classes

YOLOv7 can detect 80 COCO classes:

### Common Video Objects:

| Category | Examples |
|----------|----------|
| **People & Animals** | person, dog, cat, horse, bird |
| **Vehicles** | car, truck, bus, motorcycle, bicycle, boat, airplane |
| **Traffic** | traffic light, stop sign, parking meter |
| **Sports** | sports ball, baseball bat, skateboard, surfboard |
| **Indoor** | chair, couch, tv, laptop, cell phone, bottle |
| **Outdoor** | bench, fire hydrant, backpack, umbrella |

**Full list**: See [COCO classes](https://github.com/WongKinYiu/yolov7/blob/main/data/coco.yaml)

## 📈 Output Format

### Generated Files:

1. **Annotated Video**
   - Location: `runs/detect/video_results/your_video.mp4`
   - Contains bounding boxes with labels
   - Same resolution as input
   - Maintains original frame rate

### Video Annotations Include:
- **Bounding Box**: Rectangle around detected object
- **Class Label**: Object type (e.g., "person", "car")
- **Confidence Score**: Detection confidence (e.g., "0.92")
- **Color Coding**: Different colors for different classes

## 🛠️ Customization

### Enable Real-time Preview

```python
opt.view_img = True  # Display video while processing
```

### Detect Specific Classes Only

```python
# Only detect people (0) and cars (2)
opt.classes = [0, 2]

# Only detect vehicles
opt.classes = [1, 2, 3, 5, 7]  # bicycle, car, motorcycle, bus,
