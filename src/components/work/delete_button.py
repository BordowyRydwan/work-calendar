from kivy.uix.button import Button
from src.data.events import event
from src.helpers.file import get_db_root
from os.path import join

import os
import src.helpers.date as date_helper


class DeleteButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def delete(self, label_from, label_to):
        self.empty_inputs(label_from, label_to)
        day_data = date_helper.parse_to_file_data()

        directory_path = join(get_db_root(), day_data["directory"])
        file_path = join(directory_path, day_data["fileName"])

        if os.path.exists(file_path):
            os.remove(file_path)

        event.reload_grid()

    def empty_inputs(self, input1, input2):
        input1.content.text = ''
        input2.content.text = ''
