import gi

from binder.widgets.ModeButton import ModeButton

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Window(Gtk.ApplicationWindow):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.set_application(app)
        self.set_default_size(900, 520)
        self.set_name("main_window")

        headerbar = app.get_object("headerbar")
        pane = app.get_object("pane")
        self.modebuttons = ModeButton(app)
        self.modebuttons.connect('mode_changed', self.mode_changed)

        self.set_titlebar(headerbar)
        self.add(pane)
        self.show_all()

    def mode_changed(self, *args):
        context = self.get_style_context() # type: Gtk.StyleContext
        if context.has_class(self.modebuttons.VIEW_MODE):
            context.remove_class(self.modebuttons.VIEW_MODE)
        elif context.has_class(self.modebuttons.EDIT_MODE):
            context.remove_class(self.modebuttons.EDIT_MODE)
        context.add_class(self.modebuttons.current_mode)
