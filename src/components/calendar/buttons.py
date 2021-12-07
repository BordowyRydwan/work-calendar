from kivy.uix.button import Button

import helpers.date as dateHelper


class HiddenButton(Button):
    pass


class DaySettableButton(Button):
    def __init__(self, day, **kwargs):
        super().__init__(**kwargs)
        self.day = day
        self.on_press = self.set_day

    def set_day(self):
        dateHelper.set_day(self.day)


class NormalButton(DaySettableButton):
    pass


class TodayButton(DaySettableButton):
    pass


class WorkButton(DaySettableButton):
    pass
