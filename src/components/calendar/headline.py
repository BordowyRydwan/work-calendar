from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from helpers.months import months

import helpers.date as dateHelper
import data.date as date


class CalendarHeadline(GridLayout):
    content = StringProperty("TEST")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_month_name()

    def month_back(self):
        dateHelper.month_back()
        self.set_month_name()

    def month_forward(self):
        dateHelper.month_forward()
        self.set_month_name()

    def set_month_name(self):
        self.content = f"{months[date.calendarView.month]} {date.calendarView.year}"
