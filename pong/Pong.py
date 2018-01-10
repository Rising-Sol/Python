from kivy.app import App
from kivy.uix.widget import Widget


class Pong(Widget):
    pass


class PongApplication(App):
    def build(self):
        return Pong()


if __name__ == '__main__':
    PongApplication().run()
