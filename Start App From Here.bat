@echo off
echo Starting Hate Speech Detection App...
cd /d %~dp0
start "" /B python app.py
timeout /t 3 >nul
start http://127.0.0.1:5000/

