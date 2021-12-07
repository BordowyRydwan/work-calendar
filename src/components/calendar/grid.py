from kivy.uix.gridlayout import GridLayout

import calendar
import datetime
import data.date as date
import helpers.date as dateHelper

from os import listdir, getcwd
from os.path import isfile, join, splitext, exists
from data.events import event
from components.calendar.buttons import *


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
        monthDir = dateHelper.month_dir_for_calendar_view()
        directoryPath = f'{getcwd()}/src/database/{monthDir}'
        daysAtWork = []

        if exists(directoryPath):
            for file in listdir(directoryPath):
                if isfile(join(directoryPath, file)):
                    daysAtWork.append(int(splitext(file)[0]))

        for week in self.calendar:
            for day in week:
                button = HiddenButton()

                if day != 0:
                    button = NormalButton(text=str(day), day=day)

                if day in daysAtWork:
                    button = WorkButton(text=str(day), day=day)

                if day == today.day and dateHelper.is_month_current():
                    button = TodayButton(text=str(day), day=day)

                self.add_widget(button)
