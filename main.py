from kivy.app import App
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle, LinearGradient  


class Reg_win(App):
    def __init__(self, **kwargs):
        super(GradientBackground, self).__init__(**kwargs)
        with self.canvas.before:
            # Определяем градиент
            self.gradient = LinearGradient(pos=(0, 0), size=self.size)
            self.gradient.colors = [(1, 0, 0, 1), (0, 0, 1, 1)]  # Красный к синим
            Color(1, 1, 1, 1)  # Цвет фона
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Log_win(App):
    pass

class Main_win(App):
    pass

class Progress_win(App):
    pass


class Words_win(App):
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