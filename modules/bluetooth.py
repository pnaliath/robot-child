# modules/bluetooth.py
import socket
from modules import utils

ESP32_MAC = "00:21:13:00:12:34"   # replace with real MAC
PORT = 1
sock = None

def connect():
    global sock
    try:
        utils.log(f"Connecting to ESP32 at {ESP32_MAC}...")
        sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        sock.connect((ESP32_MAC, PORT))
        utils.log("Connected to ESP32 Bluetooth successfully!")
    except Exception as e:
        utils.log(f"[ERROR] Could not connect: {e}")
        sock = None

def send_command(cmd):
    global sock
    if sock is None:
        utils.log("[ERROR] Bluetooth not connected. Call connect() first.")
        return
    try:
        utils.log(f"Sending command: {cmd}")
        sock.send(f"{cmd}\n".encode("utf-8"))
    except Exception as e:
        utils.log(f"[ERROR] Failed to send command: {e}")

def disconnect():
    global sock
    if sock:
        utils.log("Closing Bluetooth connection...")
        sock.close()
        sock = None
