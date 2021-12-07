from kivy.uix.button import Button
from data.events import event

import os
import data.date as date


class DeleteButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def delete(self, labelFrom, labelTo):
        self.empty_inputs(labelFrom, labelTo)
        dayData = date.parse_to_file_data()

        directoryPath = f'{os.getcwd()}/src/database/{dayData["directory"]}'
        filePath = f'{directoryPath}/{dayData["fileName"]}'

        if os.path.exists(filePath):
            os.remove(filePath)

        event.reload_grid()

    def empty_inputs(self, input1, input2):
        input1.content.text = ''
        input2.content.text = ''
