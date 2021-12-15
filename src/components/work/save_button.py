from kivy.uix.button import Button
from src.data.events import event
from src.helpers.file import get_db_root
from src.components.work.popup import WorkPopup
from os.path import join

import os
import src.helpers.date as date_helper


class SaveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, label_from, label_to):
        if not self.check_inputs(label_from.content.text, label_to.content.text):
            return

        hours = [label_from.content.text, label_to.content.text]
        day_data = date_helper.parse_to_file_data()

        directory_path = join(get_db_root(), day_data["directory"])
        file_path = join(directory_path, day_data["fileName"])

        if not os.path.exists(directory_path):
            os.mkdir(directory_path)

        with open(file_path, 'w') as file:
            file.write('\n'.join(hours))

        event.reload_grid()

    def check_inputs(self, input1, input2):
        popup = WorkPopup("Błąd zapisu danych")

        if not (input1.isnumeric() and input2.isnumeric()):
            popup.error = "Wejście zawiera znaki nienumeryczne!"
            popup.open()
            return

        num1 = int(input1)
        num2 = int(input2)

        if num1 >= num2:
            popup.error = "Godzina końca zmiany jest wcześniejsza od jej początku!"
            popup.open()
            return False

        if not ((num1 in range(0, 25)) and (num2 in range(0, 25))):
            popup.error = "Godziny zawierają się w przedziale [0; 24]"
            popup.open()
            return False

        return True
