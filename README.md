# Frank Ocean Pose Detector 🎧

A Python app using **MediaPipe** and **OpenCV** to detect the iconic *Blonde* hand-over-forehead pose — when detected, it automatically plays a Frank Ocean track on Spotify. When you move away from the pose, it closes Spotify.

---

## ✨ Features
- 🧠 Real-time face + hand detection using MediaPipe  
- 👋 Detects the *Blonde* pose (hand over forehead)  
- 🎵 Automatically opens or closes Spotify  
- 🖥️ Simple, lightweight Python app

---

## 🧰 Requirements
- Python 3.8+
- Webcam
- Spotify installed (for Windows auto-open)

---

## 📦 Installation

```bash
# 1. Clone this repo
git clone https://github.com/eggeol/Frank-Ocean-Pose-Detector.git
cd frank-ocean-pose-detector

# 2. Create virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
