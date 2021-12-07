from kivy.event import EventDispatcher


class DataEventDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_date_change')
        self.register_event_type('on_month_change')
        self.register_event_type('on_save')
        self.register_event_type('on_program_start')
        super(DataEventDispatcher, self).__init__(**kwargs)

    def change_date(self, value):
        self.dispatch('on_date_change', value)

    def reload_grid(self):
        self.dispatch('on_save')

    def change_month(self):
        self.dispatch('on_month_change')

    def download_data(self):
        self.dispatch('on_program_start')

    def on_save(self, *args):
        pass

    def on_date_change(self, *args):
        pass

    def on_month_change(self, *args):
        pass

    def on_program_start(self, *args):
        pass


event = DataEventDispatcher()
