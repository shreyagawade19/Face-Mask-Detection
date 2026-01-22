# 😷 Face Mask Detection using Deep Learning

This project detects whether a person is **wearing a face mask or not** using a webcam or images.  
It uses **Deep Learning**, **OpenCV**, and **TensorFlow** with a **MobileNetV2-based CNN model**.

---

## 🚀 Features

- Real-time **face mask detection via webcam**
- Supports **image-based detection**
- Displays:
  - **Mask / No Mask label**
  - **Prediction confidence (%)**
- Uses **OpenCV DNN face detector**
- Lightweight and fast inference

---

## 🧠 Model Details

- **Base Model**: MobileNetV2 (pretrained on ImageNet)
- **Classifier**: Custom CNN head
- **Framework**: TensorFlow 2.9.0 / Keras
- **Face Detection**: Caffe-based SSD model

---

## 📂 Dataset Used

- **Name**: Face Mask Dataset
- **Source**: Kaggle
- **Classes**:
  - `with_mask`
  - `without_mask`
- **Images**: ~7,500 images (balanced)
- Images were resized to **224×224** and normalized.

---

## 📁 Project Structure

Face-Mask-Detection/
│
├── dataset/
│ ├── with_mask/
│ └── without_mask/
│
├── face_detector/
│ ├── deploy.prototxt
│ └── res10_300x300_ssd_iter_140000.caffemodel
│
├── mask_detector.model
├── detect_mask_video.py
├── detect_mask_image.py
├── train_mask_detector.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## 🛠️ Requirements

⚠️ **Important:** This project requires **specific versions** due to compatibility.

### ✅ Python Version
Python 3.9.x

shell
Copy code

### ✅ Required Libraries
numpy==1.21.6
tensorflow==2.9.0
opencv-python==4.5.5.64
scipy==1.7.3
pillow==9.5.0
matplotlib==3.5.3
imutils

yaml
Copy code

---

## 🔧 Virtual Environment Setup (Windows)

```powershell
py -3.9 -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install numpy==1.21.6
pip install tensorflow==2.9.0
pip install opencv-python==4.5.5.64 scipy==1.7.3 pillow==9.5.0 matplotlib==3.5.3 imutils
Verify installation:

powershell
Copy code
python -c "import numpy, tensorflow as tf; print(numpy.__version__, tf.__version__)"
Expected output:

Copy code
1.21.6 2.9.0
🎥 Run Face Mask Detection (Webcam)
powershell
Copy code
python detect_mask_video.py
Webcam opens automatically

Green box → Mask

Red box → No Mask

Press Q to exit

🖼️ Run Detection on Image
powershell
Copy code
python detect_mask_image.py --image path_to_image.jpg
🏋️ Train the Model (Optional)
powershell
Copy code
python train_mask_detector.py -d dataset
This will generate:

mask_detector.model

Training accuracy/loss plot

⚠️ Common Issues & Fixes
❌ NumPy 2.x Error
arduino
Copy code
A module compiled using NumPy 1.x cannot run in NumPy 2.x
✅ Fix:

nginx
Copy code
pip uninstall numpy
pip install numpy==1.21.6
❌ Webcam Not Opening
Ensure no other app is using the camera

Run from activated virtual environment

📌 Notes
GPU is optional (CPU works fine)

CUDA warnings can be ignored if no GPU is present

Do not upgrade libraries without checking compatibility

👩‍💻 Author
Shreya Gawade
Computer Engineering Student
Interested in AI, Machine Learning, and Computer Vision

⭐ Acknowledgements
TensorFlow & Keras Team

OpenCV Community

Kaggle Datasets

📜 License
This project is for educational purposes only.
