from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle


class Reg_win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)    


class Log_win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Main_win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Progress_win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Words_win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Langsea(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Reg_win(name="reg"))
        sm.add_widget(Log_win(name="log"))
        sm.add_widget(Main_win(name="main"))
        sm.add_widget(Progress_win(name="progress"))
        sm.add_widget(Words_win(name="words"))
        return sm


if __name__ == "__main__":
    Langsea().run()
