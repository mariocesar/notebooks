from typing import List

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject


class ModeButton(GObject.GObject):
    selected_action = None
    selected_widget = None

    __gsignals__ = {
        'mode_changed': (GObject.SIGNAL_RUN_FIRST, None, (str,))
    }

    def __init__(self, selected_action: str, *options: List[Gtk.RadioButton]):
        super().__init__()
        self.get_name = Gtk.Buildable.get_name

        _options = map(lambda opt: self.get_name(opt) == selected_action, options)
        assert any(_options), 'Selected action not in options'

        self.selected_action = selected_action

        for option in options:
            name = self.get_name(option)

            if name == self.selected_action:
                option.set_active(True)
                self.selected_action = name
                self.selected_widget = option

            option.connect_after('toggled', self.toggled_mode)

    def toggled_mode(self, widget: Gtk.RadioButton):
        if widget.get_active():
            self.selected_action = self.get_name(widget)
            self.selected_widget = widget

            if self.selected_widget:
                self.emit('mode_changed', self.selected_action)
