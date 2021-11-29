from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from helpers.months import months
import data.month_year as date


class CalendarHeadline(GridLayout):
    content = StringProperty("TEST")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_month_name()

    def month_back(self):
        date.month_back()
        self.set_month_name()

    def month_forward(self):
        date.month_forward()
        self.set_month_name()

    def set_month_name(self):
        self.content = f"{months[date.month]} {date.year}"
