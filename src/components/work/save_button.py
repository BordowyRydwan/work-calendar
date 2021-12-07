from kivy.uix.button import Button
from data.events import event

import os
import helpers.date as dateHelper


class SaveButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, labelFrom, labelTo):
        if not self.check_inputs(labelFrom.content.text, labelTo.content.text):
            return

        hours = [labelFrom.content.text, labelTo.content.text]
        dayData = dateHelper.parse_to_file_data()

        directoryPath = f'{os.getcwd()}/src/database/{dayData["directory"]}'
        filePath = f'{directoryPath}/{dayData["fileName"]}'

        if not os.path.exists(directoryPath):
            os.mkdir(directoryPath)

        with open(filePath, 'w') as file:
            file.write('\n'.join(hours))

        event.reload_grid()

    def check_inputs(self, input1, input2):
        if not (input1.isnumeric() and input2.isnumeric()):
            return False

        num1 = int(input1)
        num2 = int(input2)

        if num1 >= num2:
            return False

        if not ((num1 in range(0, 25)) and (num2 in range(0, 25))):
            return False

        return True
