from kivy.uix.gridlayout import GridLayout

import calendar
import datetime
import src.data.date as date
import src.helpers.date as date_helper

from os import listdir
from os.path import isfile, join, splitext, exists
from src.data.events import event
from src.helpers.file import get_db_root
from src.components.calendar.buttons import *


class CalendarGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 7
        self.rows = 6

        event.bind(on_save=self.reload_grids)
        self.set_date_props()
        self.reload_grids()

    def reload_grids(self, *args):
        self.set_date_props()
        self.clear_widgets()
        self.insert_grids()

    def set_date_props(self):
        self.calendar = calendar.monthcalendar(
            date.calendarView.year, date.calendarView.month)

    def insert_grids(self):
        today = datetime.datetime.now()
        month_dir = date_helper.month_dir_for_calendar_view()
        directory_path = join(get_db_root(), month_dir)
        days_at_work = []

        if exists(directory_path):
            for file in listdir(directory_path):
                if isfile(join(directory_path, file)):
                    days_at_work.append(int(splitext(file)[0]))

        for week in self.calendar:
            for day in week:
                button = HiddenButton()

                if day != 0:
                    button = NormalButton(text=str(day), day=day)

                if day == today.day and date_helper.is_month_current():
                    button = TodayButton(text=str(day), day=day)

                if day in days_at_work:
                    button = WorkButton(text=str(day), day=day)

                self.add_widget(button)
