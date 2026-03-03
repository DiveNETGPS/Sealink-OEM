@echo off
setlocal

cd /d "%~dp0"

echo ========================================
echo Building Windows customer release zip...
echo ========================================
call build_release.bat
if errorlevel 1 (
    echo Failed while building Windows release binaries.
    exit /b 1
)

call make_release_zip.bat
if errorlevel 1 (
    echo Failed while creating Windows release zip.
    exit /b 1
)

echo ========================================
echo Building integrator release zip...
echo ========================================
call make_integrator_zip.bat
if errorlevel 1 (
    echo Failed while creating integrator release zip.
    exit /b 1
)

echo.
echo All release packages created successfully.
echo Check the release folder for timestamped zip files.
echo.
exit /b 0
