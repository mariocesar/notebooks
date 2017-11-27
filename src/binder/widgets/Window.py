from binder.widgets.ListView import ListView
from binder.widgets.ModeButton import ModeButton


class WindowHandler:
    _widget = None

    def __init__(self, app):
        self.app = app
        self.edit_button = self.app.builder.get_object('edit_mode')
        self.view_button = self.app.builder.get_object('view_mode')

        self.modes = ModeButton('view_mode', self.edit_button, self.view_button)
        self.modes.connect('mode_changed', self.main_window_mode_changed)
        self.main_window_mode_changed()

        self.list_view = ListView(self.app)

    @property
    def widget(self):
        if not self._widget:
            self._widget = self.app.builder.get_object('main_window')
            self.app.builder.connect_signals(self)
        return self._widget

    def main_window_mode_changed(self, *args):
        context = self.widget.get_style_context()

        if context.has_class('view_mode'):
            context.remove_class('view_mode')
        elif context.has_class('edit_mode'):
            context.remove_class('edit_mode')

        context.add_class(self.modes.selected_action)
