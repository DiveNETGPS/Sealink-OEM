# Sealink-OEM – Requirements and Options

This root-level file is retained for compatibility.

## Minimum Host Requirements (Summary)

### Windows Native Utility Package
- Package: Sealink-OEM (Windows Utility package)
- OS: Windows 10 or Windows 11 (64-bit)
- Python: not required for packaged `.exe` execution
- Serial access: at least one available `COM` port through compatible USB-UART bridge or host UART interface

### Integrator / CLI Workflow
- Package: Sealink-Integrator-Pack (CLI/Integration)
- Python: 3.10 or newer (3.10–3.12 recommended)
- `pip` and dependency install from `resources/requirements.txt` (includes `pyserial`)
- Linux/Raspberry Pi workflow uses `integrations/raspberry-pi/run_sealink_cli.sh`

Current maintained version:

- [product/Sealink-OEM_Requirements_and_Options.md](product/Sealink-OEM_Requirements_and_Options.md)

Use the file above for current requirements and options guidance.

---
Questions or support? Contact DiveNET: support@divenetgps.com
Last updated: March 2026
