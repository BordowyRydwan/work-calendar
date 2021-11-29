from kivy.app import App
from kivy.config import Config

from components.calendar import *
from components.calendar.view import CalendarView

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')
Config.set('graphics', 'resizable', False)
Config.write()


class CalendarApp(App):
    kv_directory = 'views'

    def build(self):
        return CalendarView()


if __name__ == '__main__':
    CalendarApp().run()
