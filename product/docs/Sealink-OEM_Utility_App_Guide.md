# DiveNET: Sealink-OEM Utility App Guide

This guide explains how to use the Sealink-OEM Utility app and when to use the integrator workflow.

## Minimum Host Requirements

### A) Sealink-OEM (Windows Utility Package)

- OS: Windows 10 or Windows 11 (64-bit)
- No Python installation required for `.exe` usage
- At least one available serial port (`COMx`) via USB-UART adapter or direct UART bridge
- Local file write access in the package folder (for launch scripts and logs)

### B) Sealink-Integrator-Pack (Integrator CLI Package)

- Python 3.10+ (3.10-3.14 validated)
- `pip` available for dependency install
- Packages from `resources/requirements.txt` (includes `pyserial`)
- Platform workflows:
	- Windows/Linux/macOS for Python CLI script usage
	- Raspberry Pi/Linux shell script usage under `integrations/raspberry-pi`
	- Arduino IDE for `integrations/arduino/SealinkOEM_Basic.ino`
- Detailed venv creation/activation commands are documented in `integrations/PLATFORM_INTEGRATOR_GUIDE.md`.

## 1. Scope

The Utility app is intended for:

- Initial product familiarization
- Basic command execution and response verification
- Essential functionality/performance checks

## 2. Windows Utility Workflow

In the Sealink-OEM package folder:

Main Files:

- `SealinkUtility.exe` (main app)
- `SealinkListener.exe` (test/demo listener)
- `run_utility.bat` (start utility only)
- `run_listener.bat` (start listener only)
- `run_all.bat` (start listener + utility)

Typical Use:

1. Connect hardware and identify COM port.
2. Start `run_utility.bat`.
3. Enter serial port, channels, and environmental parameters in the app.
4. Select command (`ping`, `device-info`, or `remote-depth`) and run.

## 3. Source Repository Workflow (Python, optional)

If you are working from the source repository (not a packaged download):

- Start utility: `launch_utility.bat`
- Start listener only: `launch_listener.bat`
- Start both windows: `start_all.bat`
- Quiet start: `start_all_quiet.bat`

Underlying script:

- `product/resources/sealink_utility.py`

## 4. Utility Inputs

Required/Typical Fields:

- Serial port (for example `COM3`)
- TX channel
- RX channel
- Depth (m)
- Temperature (°C)
- Salinity (PSU)
- Command selection

The app computes sound speed from environmental values and reports propagation time and slant range from responses.

## 5. Relationship to CLI Test Script

The Utility app wraps the same command logic used by:

- `product/resources/uart-getRange.py`

Use the script directly when CLI automation is preferred.

## 6. Troubleshooting

- Port open error: verify COM port and close other serial tools.
- No response: verify wiring, transducer connection, channel match, and acoustic path.
- Unstable results: collect multiple pings and average under stable conditions.

For protocol-level details, see [Sealink-OEM Communication Protocol](Sealink-OEM_Communication_Protocol.md).

---
Questions or support? Contact DiveNET: support@divenetgps.com
Last updated: March 2026
