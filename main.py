from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello Papa, robot-child is ready!")

if __name__ == "__main__":
    MyApp().run()
