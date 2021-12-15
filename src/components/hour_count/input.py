from kivy.uix.textinput import TextInput
from os import listdir
from os.path import join, exists

from src.data.events import event
from src.helpers.file import get_db_root
import src.helpers.date as date_helper


class HourCountInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        event.bind(on_save=self.fill_text)
        event.bind(on_month_change=self.fill_text)
        self.fill_text()

    def fill_text(self, *args):
        month_dir = date_helper.month_dir_for_calendar_view()
        directory_path = join(get_db_root(), month_dir)
        hours_sum = 0

        if not exists(directory_path):
            self.text = str(hours_sum)
            return

        files = listdir(directory_path)

        for fileName in files:
            with open(join(directory_path, fileName)) as file:
                num1 = int(file.readline().rstrip())
                num2 = int(file.readline().rstrip())

                hours_sum += num2 - num1

        self.text = str(hours_sum)
