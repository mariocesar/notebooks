import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject


class ModeButton(GObject.GObject):
    EDIT_MODE = 'edit_mode'
    VIEW_MODE = 'view_mode'

    _mode = VIEW_MODE

    __gsignals__ = {
        'mode_changed': (GObject.SIGNAL_RUN_FIRST, None, (str,))
    }

    def __init__(self, app):
        super().__init__()

        edit_button = app.get_object(self.EDIT_MODE)  # type: Gtk.RadioButton
        view_button = app.get_object(self.VIEW_MODE)  # type: Gtk.RadioButton

        view_button.join_group(edit_button)
        view_button.set_active(True)

        edit_button.connect_after('toggled', self.toggled_mode)
        view_button.connect_after('toggled', self.toggled_mode)

    @property
    def current_mode(self):
        return self._mode

    @current_mode.setter
    def current_mode(self, value):
        if value not in (self.EDIT_MODE, self.VIEW_MODE):
            raise ValueError("Wrong mode")
        self._mode = value
        self.emit('mode_changed', self._mode)

    def toggled_mode(self, widget: Gtk.RadioButton):
        if widget.get_active():
            self.current_mode = Gtk.Buildable.get_name(widget)
