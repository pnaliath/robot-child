# modules/utils.py
import time

def log(msg):
    ts = time.strftime("[%H:%M:%S]")
    print(f"{ts} {msg}")
