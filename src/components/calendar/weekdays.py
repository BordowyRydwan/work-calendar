from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from helpers.weekdays import days


class CalendarWeekdays(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 7
        self.fill_cols()

    def fill_cols(self):
        for day in days:
            self.add_widget(Label(text=day))
