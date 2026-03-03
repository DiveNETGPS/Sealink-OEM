@echo off
setlocal

REM Move to this BAT's folder (workspace root)
cd /d "%~dp0"

set "SCRIPT=test_listener.py"

if not exist "%SCRIPT%" (
    echo Could not find %SCRIPT%
    pause
    exit /b 1
)

echo Starting listener...

REM Prefer local virtual environment if present
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" "%SCRIPT%"
    goto :done
)

REM Fallback to system Python launcher
where py >nul 2>nul
if %errorlevel%==0 (
    py "%SCRIPT%"
    goto :done
)

where python >nul 2>nul
if %errorlevel%==0 (
    python "%SCRIPT%"
    goto :done
)

echo Python was not found. Install Python or create a .venv in this folder.

:done
echo.
echo Listener exited. Press any key to close.
pause >nul
exit /b 0
