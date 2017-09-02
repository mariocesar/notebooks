import os

import gi

from binder.widgets.Window import Window

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk, GObject
from gi.repository import GtkSource



class Application(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, flags=Gio.ApplicationFlags.FLAGS_NONE)
        GObject.type_register(GtkSource.View)

        self.running = False
        self.license_type = Gtk.License.GPL_2_0
        self.set_application_id('com.github.mariocesar.notebooks')
        self.program_name = 'binder'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.path.dirname(__file__), 'data/main.ui'))
        self.get_object = self.builder.get_object

    def do_activate(self):
        if not self.running:
            self.window = Window(self)
            self.add_window(self.window)
            self.running = True

        self.window.show()
