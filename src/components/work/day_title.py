from kivy.uix.label import Label
import data.date as date


class WorkDayTitle(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_title()
        date.event.bind(on_date_change=self.set_title)

    def set_title(self, *args):
        self.text = f"{date.selected.day}.{date.selected.month}.{date.selected.year}"
