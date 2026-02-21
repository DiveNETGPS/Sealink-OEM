import serial
import time

def calculate_nmea_checksum(sentence):
    """NMEA checksum: XOR of bytes after $ up to * (excluding $)"""
    chk = 0
    for char in sentence[1:]:  # skip $
        chk ^= ord(char)
    return f"{chk:02X}".upper()

def send_rc_ping(ser, tx_ch=0, rx_ch=0):
    cmd_body = f"PUWV,RC,{tx_ch},{rx_ch},0"
    checksum = calculate_nmea_checksum(cmd_body)
    full_cmd = f"${cmd_body}*{checksum}\r\n"
    ser.write(full_cmd.encode('ascii'))
    print(f"Sent ping: {full_cmd.strip()}")

def read_response(ser, timeout_sec=5):
    start_time = time.time()
    while time.time() - start_time < timeout_sec:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        if not line:
            continue
        print(f"Received: {line}")
        
        if line.startswith('$PUWV,RC,'):
            parts = line.split(',')
            if len(parts) >= 3:
                try:
                    tp_sec = float(parts[2])  # propagation time
                    distance_m = tp_sec * 1500 / 2  # adjust sound speed as needed
                    print(f"Propagation time: {tp_sec:.4f} s → Slant range: {distance_m:.1f} m")
                    return tp_sec, distance_m
                except ValueError:
                    print("Failed to parse tp value")
        time.sleep(0.05)
    print("No RC_PING response received within timeout")
    return None, None

# Usage example
if __name__ == "__main__":
    ser = serial.Serial(
        port='COM3',          # ← customer changes this (Windows: COMx, Linux/Mac: /dev/ttyUSBx or /dev/ttyACM0)
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    try:
        send_rc_ping(ser, tx_ch=0, rx_ch=0)  # use your known channels
        time.sleep(0.5)  # short delay for acoustic travel
        tp, distance = read_response(ser, timeout_sec=10)  # increase if long range
    finally:
        ser.close()
