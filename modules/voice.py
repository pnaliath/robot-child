# modules/voice.py
from modules import utils

def listen():
    utils.log("Listening (mock)...")
    return None  # Replace with real speech recognition later

def respond(text):
    utils.log(f"Robot says: {text}")
