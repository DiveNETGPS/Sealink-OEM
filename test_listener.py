"""
Simple listener for testing - run this in a separate terminal first.
"""
import argparse
import serial
import time


def parse_args():
    parser = argparse.ArgumentParser(description='Sealink test listener')
    parser.add_argument('--port', default='COM7', help='Serial port to open (default: COM7)')
    parser.add_argument('--duration', type=int, default=120, help='Listen duration in seconds (default: 120)')
    return parser.parse_args()


args = parse_args()
port_name = args.port
listen_duration = args.duration

try:
    print(f"Opening {port_name} for listening...")
    ser = serial.Serial(
        port=port_name,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    print(f"{port_name} opened successfully. Listening for {listen_duration} seconds...")
    
    start_time = time.time()
    while time.time() - start_time < listen_duration:
        line = ser.readline()
        if line:
            text = line.decode('ascii', errors='ignore').strip()
            print(f"Received: {text}")
            # reply to numeric-format remote code request (PUWV2)
            if text.startswith('$PUWV2,'):
                # parse fields to echo back channels and rcCmdID
                parts = text.split(',')
                # expect [$PUWV2,tx,rx,cmdID*hh]
                if len(parts) >= 4:
                    try:
                        tx = parts[1]
                        rcid_field = parts[3]
                        # strip checksum part if attached
                        if '*' in rcid_field:
                            rcid = rcid_field.split('*')[0]
                        else:
                            rcid = rcid_field
                    except Exception:
                        tx = '0'; rcid = '0'
                else:
                    tx = '0'; rcid = '0'
                # craft response: $PUWV3,txChID,rcCmdID,propTime,MSR*hh
                resp_body = f"PUWV3,{tx},{rcid},0.1234,0"
                chk = 0
                for ch in resp_body[1:]:
                    chk ^= ord(ch)
                checksum = f"{chk:02X}".upper()
                full = f"${resp_body}*{checksum}\r\n"
                ser.write(full.encode('ascii'))
                print(f"Sent back: {full.strip()}")
            # reply to device info request (PUWV?)
            elif text.startswith('$PUWV?'):
                # device info response format: $PUWV!,serialNumber,systemMoniker,systemVersion,...*hh
                resp_body = "PUWV!,TEST0001,SEALINK,1.00,SEALINK_CORE,1.01,9600,0,0,20,35.0,1,1"
                chk = 0
                for ch in resp_body[1:]:
                    chk ^= ord(ch)
                checksum = f"{chk:02X}".upper()
                full = f"${resp_body}*{checksum}\r\n"
                ser.write(full.encode('ascii'))
                print(f"Sent back: {full.strip()}")
        time.sleep(0.1)
    
    ser.close()
    print(f"{port_name} closed.")
except Exception as e:
    print(f"Error: {e}")
