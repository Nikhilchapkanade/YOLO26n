# 🚀 YOLO26 Traffic Analytics System

![YOLO26 Banner](https://img.shields.io/badge/YOLO-v26-blue) ![Python](https://img.shields.io/badge/Python-3.12-yellow) ![PyTorch](https://img.shields.io/badge/PyTorch-2.4%2B-red) ![License](https://img.shields.io/badge/License-MIT-green)

A practical computer vision project that uses the latest **YOLO26** model to analyze traffic from drone footage. Built to work with the **VisDrone** dataset and optimized to run smoothly on standard CPUs.

---

## 🌟 Key Features

* ⚡ **Lightning Fast:** YOLO26's end-to-end detection skips slow post-processing steps.
* 🧠 **Smart Training:** Uses the new MuSGD Optimizer to detect tiny vehicles accurately.
* 🚁 **Drone-Ready:** Trained specifically on aerial views to spot cars, trucks, and buses.
* 🚦 **Vehicle Counting:** Tracks and counts vehicles crossing virtual road lines.
* 💻 **CPU Friendly:** Runs well on standard computers - no expensive GPU needed.

---

## 🎥 Demo & Results

**Sample Detection Output:**

<img width="100%" alt="Screenshot 2026-01-26 195538" src="https://github.com/user-attachments/assets/d06d484e-f4d2-476b-9683-c6a72c569f3b" />

*Vehicle detection with bounding boxes, confidence scores, and real-time counting.*

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Model** | YOLO26n (Nano) - Ultralytics |
| **Language** | Python 3.12 |
| **Framework** | PyTorch 2.4+ |
| **Vision** | OpenCV |
| **Dataset** | VisDrone2019 (6.5GB, ~10k images) |
| **Training** | NVIDIA T4 GPU (Google Colab Pro) |

---

## 📂 Project Structure

```text
YOLO26-Advanced-Project/
├── data/
│   └── traffic.mp4          # Test video file
├── models/
│   ├── yolo26n.pt           # Base YOLO26 model
│   └── best.pt              # Custom trained model
├── outputs/
│   ├── videos/              # Processed videos
│   ├── images/              # Detection screenshots
│   └── logs/                # Count statistics
├── src/
│   ├── trainer.py           # Training logic
│   ├── inference.py         # Detection engine
│   └── config.py            # Configuration
├── main.py                  # General detection script
├── traffic_counter.py       # Vehicle counting script
├── requirements.txt         # Dependencies
└── README.md                # Documentation
⚙️ Installation
Step 1: Clone Repository

Bash
git clone [https://github.com/Nikhilchapkanade/YOLO26-.git](https://github.com/Nikhilchapkanade/YOLO26-.git)
cd YOLO26-
Step 2: Install Dependencies

Bash
pip install -r requirements.txt
Step 3: Setup Model

Place your trained model best.pt in the models/ directory.

🚀 Usage
Option 1: Vehicle Counting (Primary Feature)
Count vehicles crossing a virtual line on the road:

Bash
python traffic_counter.py
Tip: Edit path_to_video inside traffic_counter.py to use your own video.

Option 2: General Object Detection
Detect objects without counting:

Analyze a video file:

Bash
python main.py --mode predict --source "data/traffic.mp4"
Use webcam:

Bash
python main.py --mode predict --source 0
🧠 Model Training Details
The model was fine-tuned with the following configuration:

Epochs: 20 (Early Stopping enabled)

Batch Size: 16

Image Size: 640x640

Precision: Mixed (FP16)

Optimizer: MuSGD (Optimized for Stability)

Hardware: NVIDIA T4 GPU

🔮 Future Roadmap
[ ] Speed Estimation: Calculate vehicle speeds using perspective transform.

[ ] Database Integration: Store traffic data in SQL database.

[ ] Multi-Lane Tracking: Separate counts for each lane.

[ ] Web Dashboard: Real-time visualization in browser.

[ ] Edge Deployment: Run on Raspberry Pi 5 with Hailo-8.

🤝 Contributing
Contributions are welcome!

Fork the repository.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit changes (git commit -m 'Add AmazingFeature').

Push to branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📝 License
This project is licensed under the MIT License.
