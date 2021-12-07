from kivy.uix.boxlayout import BoxLayout
from data.events import event

import data.date as date
import os


class WorkInputs(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        event.bind(on_date_change=self.load_info)
        event.bind(on_program_start=self.load_info)

    def load_info(self, *args):
        inputTo, inputFrom = self.children[2:4]

        dayData = date.parse_to_file_data()

        directoryPath = f'{os.getcwd()}/src/database/{dayData["directory"]}'
        filePath = f'{directoryPath}/{dayData["fileName"]}'

        if not os.path.exists(filePath):
            inputFrom.content.text = ''
            inputTo.content.text = ''
            return

        with open(filePath, 'r') as file:
            inputFrom.content.text = file.readline().rstrip()
            inputTo.content.text = file.readline().rstrip()
