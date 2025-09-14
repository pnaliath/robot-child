import threading, queue, time
from modules import bluetooth, voice, utils
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

event_queue = queue.Queue()

# Background workers
def bluetooth_worker():
    bluetooth.connect()
    while True:
        time.sleep(0.5)

def voice_worker():
    while True:
        cmd = voice.listen()
        if cmd:
            event_queue.put(("voice_cmd", cmd))
        time.sleep(1)

def logic_worker():
    while True:
        try:
            event_type, data = event_queue.get(timeout=1)
            if event_type == "voice_cmd":
                utils.log(f"Logic received: {data}")
                if "forward" in data:
                    bluetooth.send_command("F200")
                elif "back" in data:
                    bluetooth.send_command("B200")
                elif "stop" in data:
                    bluetooth.send_command("S")
        except queue.Empty:
            pass

# Kivy UI
class RobotUI(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        layout.add_widget(Image(source="assets/images/unicorn.png"))

        kill_btn = Button(text="KILL SWITCH", background_color=(1, 0, 0, 1))
        kill_btn.bind(on_press=self.kill_robot)
        layout.add_widget(kill_btn)

        settings_btn = Button(text="⚙ Settings")
        settings_btn.bind(on_press=self.open_settings)
        layout.add_widget(settings_btn)

        return layout

    def kill_robot(self, instance):
        bluetooth.send_command("S")
        utils.log("KILL SWITCH PRESSED. Robot stopped.")

    def open_settings(self, instance):
        utils.log("Settings menu coming soon...")

if __name__ == "__main__":
    threading.Thread(target=bluetooth_worker, daemon=True).start()
    threading.Thread(target=voice_worker, daemon=True).start()
    threading.Thread(target=logic_worker, daemon=True).start()
    RobotUI().run()
