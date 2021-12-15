from kivy.uix.button import Button
import src.helpers.date as date_helper


class DaySettableButton(Button):
    def __init__(self, day, **kwargs):
        super().__init__(**kwargs)
        self.day = day
        self.on_press = self.set_day

    def set_day(self):
        date_helper.set_day(self.day)


class HiddenButton(Button):
    pass


class NormalButton(DaySettableButton):
    pass


class TodayButton(DaySettableButton):
    pass


class WorkButton(DaySettableButton):
    pass
