import gi

from binder.widgets.Headerbar import Headerbar

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GtkSource


class Window(Gtk.ApplicationWindow):
    def __init__(self, app: Gtk.Application, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.set_default_size(1100, 640)
        self.set_titlebar(Headerbar())

        pane1 = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)

        view = GtkSource.View()
        view.set_can_focus(True)
        view.set_visible(True)

        sidebar = Gtk.Layout()

        pane1.add1(sidebar)
        pane1.add2(view)
        pane1.set_position(180)
        pane1.show_all()

        self.add(pane1)
        self.show_all()
