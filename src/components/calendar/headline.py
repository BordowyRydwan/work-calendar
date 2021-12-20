from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from src.helpers.months import months

import src.helpers.date as date_helper
import src.data.date as date


class CalendarHeadline(GridLayout):
    content = StringProperty()
    rows = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_month_name()

    def month_back(self):
        date_helper.month_back()
        self.set_month_name()

    def month_forward(self):
        date_helper.month_forward()
        self.set_month_name()

    def set_month_name(self):
        self.content = f"{months[date.calendarView.month]} {date.calendarView.year}"
