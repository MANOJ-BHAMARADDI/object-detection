
---

```markdown
# 📱 Phone Detection with YOLOv8

## 📌 Overview  
This project performs real-time mobile phone detection using **YOLOv8** and your webcam. It uses OpenCV to capture frames and Ultralytics' YOLOv8 model for object detection. Built as a simple and beginner-friendly computer vision project.

---

## 🚀 Features
- **🧠 Real-Time Detection**: Detects phones and other common objects live through your webcam.
- **📦 YOLOv8 Integration**: Uses Ultralytics' YOLOv8 Nano model (`yolov8n.pt`) for fast inference.
- **📸 Webcam Feed with FPS**: Displays bounding boxes and current FPS on screen.
- **🔁 Easily Extendable**: Train a custom model (`best.pt`) for more precise or unique detections.

---

## 🛠️ Tech Stack

### Core:
- Python
- OpenCV
- YOLOv8 (Ultralytics)

### Tools:
- VS Code
- Git & GitHub

---

## 📂 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MANOJ-BHAMARADDI/object-detection.git
cd object-detection
```

### 2️⃣ Create and Activate Virtual Environment (Recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install ultralytics opencv-python
```

### 4️⃣ Run the Detection Script
```bash
python phone_detector.py
```

---

## 🔍 Model Options

- **`yolov8n.pt`**: Default pretrained model that detects general objects like `person`, `cell phone`, etc.
- **`best.pt`** *(optional)*: Your custom-trained YOLOv8 model for specific object detection (e.g., only mobile phones).

> Make sure the `.pt` file is in the project root or update the path in the script.

---

---

## 🧠 Future Improvements
- ✅ Real-time phone detection  
- 🚧 Custom training for brand-specific phones  
- 🚀 Streamlit or Gradio UI for easier demos  
- 💡 Deploy to web or desktop app


### 👨‍💻 Created by [Manoj Bhamaraddi](https://github.com/MANOJ-BHAMARADDI)
```

---