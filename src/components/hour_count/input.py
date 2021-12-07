from kivy.uix.textinput import TextInput
from os import listdir, getcwd
from os.path import join, exists

from data.events import event
import helpers.date as dateHelper


class HourCountInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        event.bind(on_save=self.fill_text)
        event.bind(on_month_change=self.fill_text)
        self.fill_text()

    def fill_text(self, *args):
        monthDir = dateHelper.month_dir_for_calendar_view()
        directoryPath = f'{getcwd()}/src/database/{monthDir}'
        sum = 0

        if not exists(directoryPath):
            self.text = str(sum)
            return

        files = listdir(directoryPath)

        for fileName in files:
            with open(join(directoryPath, fileName)) as file:
                num1 = int(file.readline().rstrip())
                num2 = int(file.readline().rstrip())

                sum += num2 - num1

        self.text = str(sum)
