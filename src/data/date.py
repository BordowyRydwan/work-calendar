from kivy.event import EventDispatcher
from data.events import event

import datetime


class Date():
    def __init__(self):
        self.day = datetime.datetime.now().day
        self.month = datetime.datetime.now().month
        self.year = datetime.datetime.now().year


selected = Date()
calendarView = Date()
base = Date()
