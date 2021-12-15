from kivy.properties import StringProperty
from kivy.uix.popup import Popup


class WorkPopup(Popup):
    error = StringProperty(None)

    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.title = title
