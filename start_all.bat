@echo off
setlocal

REM Move to this BAT's folder (workspace root)
cd /d "%~dp0"

set "LISTENER=test_listener.py"
set "GUI=Sealink-OEM-main\resources\sealink_gui.py"

if not exist "%LISTENER%" (
    echo Could not find %LISTENER%
    pause
    exit /b 1
)

if not exist "%GUI%" (
    echo Could not find %GUI%
    pause
    exit /b 1
)

REM Decide which Python command to use
set "PYCMD="
if exist ".venv\Scripts\python.exe" set "PYCMD=.venv\Scripts\python.exe"

if not defined PYCMD (
    where py >nul 2>nul
    if %errorlevel%==0 set "PYCMD=py"
)

if not defined PYCMD (
    where python >nul 2>nul
    if %errorlevel%==0 set "PYCMD=python"
)

if not defined PYCMD (
    echo Python was not found. Install Python or create a .venv in this folder.
    pause
    exit /b 1
)

echo Using: %PYCMD%
echo Starting listener window...
start "Sealink Listener" cmd /k "%PYCMD% "%LISTENER%""

timeout /t 1 /nobreak >nul

echo Starting GUI window...
start "Sealink GUI" cmd /k "%PYCMD% "%GUI%""

echo.
echo Both processes launched.
echo You can close this launcher window.
exit /b 0
