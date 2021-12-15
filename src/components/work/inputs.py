from kivy.uix.boxlayout import BoxLayout
from src.data.events import event
from src.helpers.file import get_db_root
from os.path import join

import src.helpers.date as date_helper
import os


class WorkInputs(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        event.bind(on_date_change=self.load_info)
        event.bind(on_program_start=self.load_info)

    def load_info(self, *args):
        input_to, input_from = self.children[2:4]

        day_data = date_helper.parse_to_file_data()
        directory_path = join(get_db_root(), day_data["directory"])
        file_path = join(directory_path, day_data["fileName"])

        if not os.path.exists(file_path):
            input_from.content.text = ''
            input_to.content.text = ''
            return

        with open(file_path, 'r') as file:
            input_from.content.text = file.readline().rstrip()
            input_to.content.text = file.readline().rstrip()
