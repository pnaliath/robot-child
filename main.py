import os
import sys
import subprocess

# Path to requirements.txt (same folder as main.py)
REQ_FILE = os.path.join(os.path.dirname(__file__), "requirements.txt")

def install_requirements():
    """Check and install missing dependencies from requirements.txt"""
    if os.path.exists(REQ_FILE):
        print("[INFO] Checking dependencies...")
        try:
            # Try importing a critical dependency to test environment
            import kivy
        except ImportError:
            print("[INFO] Kivy not found, installing all requirements...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", REQ_FILE])
        else:
            print("[INFO] Dependencies already installed.")
    else:
        print("[WARNING] requirements.txt not found! Skipping auto-install.")

# Run dependency check before launching the app
install_requirements()

# ---- Your Kivy App Starts Here ----
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello from Robot Child with Auto Installer!")

if __name__ == "__main__":
    MyApp().run()
