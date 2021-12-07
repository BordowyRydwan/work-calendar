from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class InputLabel(BoxLayout):
    content = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
