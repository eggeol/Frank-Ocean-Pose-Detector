@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
python src\pose_detector.py
