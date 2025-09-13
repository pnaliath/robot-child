from kivy.app import App
from kivy.uix.label import Label
from app import config


class RobotChild(App):
    def build(self):
        # For now, just a hello screen
        return Label(text="Hello Papa, I am ready!")


if __name__ == "__main__":
    RobotChild().run()
