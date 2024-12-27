from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, LinearGradient  


class Reg_win(Screen):
    pass


class Log_win(Screen):
    pass

class Main_win(Screen):
    pass

class Progress_win(Screen):
    pass


class Words_win(Screen):
    pass





class Langsea(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Reg_win(name="reg"))
        sm.add_widget(Log_win(name="log"))
        sm.add_widget(Main_win(name="main"))
        sm.add_widget(Progress_win(name="progress"))
        sm.add_widget(Words_win(name="words"))
     
        return sm
        




if __name__ == 'main':
    Langsea().run()