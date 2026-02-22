<p align="center">
  <h1 align="center">👁️ YOLO26n Traffic Analytics</h1>
  <p align="center"><strong>Real-time vehicle detection, tracking & counting with the latest YOLO26</strong></p>
  <p align="center"><em>Detects, tracks, and counts cars in drone footage — optimized for CPU inference.</em></p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/YOLO-v26-0099FF?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-2.4+-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
</p>

---

## 📸 Demo

<img width="100%" alt="YOLO26n Detection" src="https://github.com/user-attachments/assets/d06d484e-f4d2-476b-9683-c6a72c569f3b" />

*Vehicle detection with bounding boxes, confidence scores, and real-time counting.*

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| 🚀 **YOLO26 End-to-End** | Skips slow NMS post-processing for faster inference |
| 🧠 **MuSGD Optimizer** | New optimizer for stable training on tiny objects |
| 🚁 **Drone-Ready** | Trained on VisDrone dataset (10k aerial images) |
| 🚦 **Vehicle Counting** | Tracks vehicles crossing virtual counting lines |
| 💻 **CPU Friendly** | Runs smoothly without a GPU |

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Nikhilchapkanade/YOLO26n.git
cd YOLO26n

# 2. Install
pip install -r requirements.txt

# 3. Run vehicle counting
python traffic_counter.py

# 4. Or general detection
python main.py --mode predict --source "data/traffic.mp4"

# 5. Webcam mode
python main.py --mode predict --source 0
```

---

## 🏋️ Training Details

| Parameter | Value |
|-----------|-------|
| Epochs | 20 (early stopping) |
| Batch Size | 16 |
| Image Size | 640×640 |
| Precision | Mixed FP16 |
| Optimizer | MuSGD |
| Hardware | NVIDIA T4 (Colab Pro) |
| Dataset | VisDrone2019 (6.5GB, ~10k images) |

---

## 📁 Project Structure

```
YOLO26n/
├── main.py               # General detection script
├── traffic_counter.py     # Vehicle counting with line crossing
├── src/
│   ├── trainer.py         # Training pipeline
│   ├── inference.py       # Detection engine
│   └── config.py          # Configuration
├── models/
│   ├── yolo26n.pt         # Base YOLO26 nano model
│   └── best.pt            # Custom trained weights
├── data/
│   └── traffic.mp4        # Test video
└── requirements.txt
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Model | YOLO26n (Nano) — Ultralytics |
| Framework | PyTorch 2.4+ |
| Vision | OpenCV |
| Dataset | VisDrone2019 |
| Training | NVIDIA T4 GPU (Google Colab) |

---

## 🔮 Future Roadmap

- [ ] Speed estimation via perspective transform
- [ ] SQL database for traffic data storage
- [ ] Multi-lane tracking with per-lane counts
- [ ] Real-time web dashboard
- [ ] Edge deployment on Raspberry Pi 5 + Hailo-8
