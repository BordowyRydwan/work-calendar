from kivy.app import App
from kivy.config import Config

from components.calendar import *
from components.work import *
from components.hour_count import *
from data.events import event

from components.calendar.view import CalendarView

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()


class CalendarApp(App):
    kv_directory = 'views'

    def build(self):
        self.root = CalendarView()
        return self.root

    def on_start(self):
        event.download_data()


if __name__ == '__main__':
    CalendarApp().run()
