Sealink-OEM Windows Package
===========================

This folder includes:
- SealinkUtility.exe    (main utility app)
- SealinkListener.exe   (test listener)
- run_utility.bat       (launch utility only)
- run_listener.bat      (launch listener only)
- run_all.bat           (launch listener + utility)

Quick start:
1) Connect your hardware and identify the COM port.
2) Double-click run_utility.bat for normal operation.
3) If you need the built-in test listener (bench testing or demo), double-click run_all.bat.

Virtual COM simulation:
- For bench testing without hardware, use a virtual COM port pair and run_all.bat.
- run_all.bat starts SealinkListener.exe plus the utility to simulate protocol responses.

Troubleshooting:
- If Windows SmartScreen warns, click "More info" then "Run anyway" (if trusted source).
- Ensure the serial device appears in Device Manager.
- Listener is only for test workflows without actual hardware connected; typical users run utility only connected to hardware.
