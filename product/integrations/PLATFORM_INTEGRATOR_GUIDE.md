# Sealink OEM Integrator Platform Guide

## Which package should you use?

Choose the package that matches your workflow.

### Package A: `Sealink-OEM` (Windows Utility package)
Use this package for normal Windows operation with the desktop utility.

This is the turnkey Windows Utility package with `.exe` binaries and `.bat` launchers for normal day-to-day use.

See `docs/Sealink-OEM_Utility_App_Guide.md` for app-specific usage details.

### Package B: `Sealink-Integrator-Pack` (Technical integration package)
Use this package if you are integrating on Raspberry Pi/Linux or Arduino.

This package covers Linux/Raspberry Pi and Arduino workflows in a single technical bundle.

## Python Environment Setup (Integrator CLI)

Run these commands from the `Sealink-Integrator-Pack` root folder.

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r resources\requirements.txt
```

If PowerShell blocks script execution:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Linux / Raspberry Pi / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r resources/requirements.txt
```

### Basic CLI Validation
```bash
python resources/uart-getRange.py --port <PORT> --test ping --tx 0 --rx 0
```

Replace `<PORT>` with the host serial interface (for example `COM3` on Windows or `/dev/ttyUSB0` on Linux).

## Integrator targets included

### Raspberry Pi / Linux
Files:
- `resources/uart-getRange.py`
- `resources/requirements.txt`
- `integrations/raspberry-pi/run_sealink_cli.sh`

Quick start on Raspberry Pi:
```bash
cd integrations/raspberry-pi
chmod +x run_sealink_cli.sh
./run_sealink_cli.sh --port /dev/ttyUSB0 --test ping --tx 0 --rx 0
```

Notes:
- UART protocol is `9600 8N1`.
- For onboard UART (GPIO), port is commonly `/dev/serial0`.
- CLI is preferred for headless/system integration.

### Arduino / MCU
File:
- `integrations/arduino/SealinkOEM_Basic.ino`

What it does:
- Builds proper `$PUWV...*hh` checksum sentences.
- Sends device info request (`PUWV?,0`) and remote ping (`PUWV2,tx,rx,0`).
- Parses `PUWV3` propagation time and prints approximate range.

Hardware requirements:
- 3.3V UART logic compatible with Sealink-OEM.
- Board with a hardware UART connected to modem (example sketch uses `Serial1`).

## macOS support
There is no separate macOS desktop package.

For macOS, use the CLI workflow with the same steps shown for Linux.

---
Questions or support? Contact DiveNET: support@divenetgps.com
Last updated: March 2026
