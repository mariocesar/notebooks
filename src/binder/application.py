import os

import gi

from binder.widgets.Window import Window

gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GObject
from gi.repository import GtkSource


class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, flags=Gio.ApplicationFlags.FLAGS_NONE)
        GObject.type_register(GtkSource.View)
        self.program_name = 'binder'
        self.license_type = Gtk.License.GPL_2_0
        self.running = False
        self.set_application_id('com.github.mariocesar.binder')

        self.builder = Gtk.Builder()
        self.builder.set_application(self)
        self.builder.add_from_file(os.path.join(os.path.dirname(__file__), 'data/main.glade'))

        self.get_object = self.builder.get_object

    def get_main_window(self):
        window = Window(self)
        provider = Gtk.CssProvider()
        provider.load_from_path(os.path.join(os.path.dirname(__file__), 'data/application.css'))

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        return window

    def do_activate(self):
        if not self.running:
            self.window = self.get_main_window()
            self.add_window(self.window)
            self.running = True

        self.window.show()
