from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import data.month_year as date
import calendar
import datetime


class HiddenButton(Button):
    pass


class NormalButton(Button):
    pass


class TodayButton(Button):
    pass


class CalendarGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 7
        self.rows = 6

        self.set_date_props()
        self.reload_grids()

    def reload_grids(self):
        self.set_date_props()
        self.clear_widgets()
        self.insert_grids()

    def set_date_props(self):
        self.calendar = calendar.monthcalendar(date.year, date.month)

    def insert_grids(self):
        today = datetime.datetime.now()

        for week in self.calendar:
            for day in week:
                if day == today.day and date.is_month_current():
                    self.add_widget(TodayButton(text=str(day)))
                elif day != 0:
                    self.add_widget(NormalButton(text=str(day)))
                else:
                    self.add_widget(HiddenButton())
