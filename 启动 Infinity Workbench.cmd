@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\pythonw.exe" (
  echo Missing .venv. Run: py -3.11 -m venv .venv
  pause
  exit /b 1
)
start "Infinity Workbench Server" /min ".venv\Scripts\pythonw.exe" -m streamlit run app.py --server.port 8501 --server.address 127.0.0.1 --server.headless true --server.fileWatcherType none --browser.gatherUsageStats false
ping -n 8 127.0.0.1 >nul 2>&1
start "" "http://127.0.0.1:8501"
exit /b 0