@echo off
setlocal

REM Move to this BAT's folder (workspace root)
cd /d "%~dp0"

set "SCRIPT=Sealink-OEM-main\resources\sealink_gui.py"

if not exist "%SCRIPT%" (
    echo Could not find %SCRIPT%
    pause
    exit /b 1
)

REM Prefer local virtual environment if present
if exist ".venv\Scripts\pythonw.exe" (
    start "" ".venv\Scripts\pythonw.exe" "%SCRIPT%"
    exit /b 0
)

if exist ".venv\Scripts\python.exe" (
    start "" ".venv\Scripts\python.exe" "%SCRIPT%"
    exit /b 0
)

REM Fallback to system Python launcher
where py >nul 2>nul
if %errorlevel%==0 (
    start "" py "%SCRIPT%"
    exit /b 0
)

where python >nul 2>nul
if %errorlevel%==0 (
    start "" python "%SCRIPT%"
    exit /b 0
)

echo Python was not found. Install Python or create a .venv in this folder.
pause
exit /b 1
