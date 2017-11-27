from datetime import datetime
from typing import List

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Pango, GObject


class ListView(GObject.GObject):

    __gsignals__ = {
        'item_selected': (GObject.SIGNAL_RUN_FIRST, None, (str,))
    }

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.widget = self.app.builder.get_object('notes_list_view')

        for n in range(100):
            box = Gtk.VBox()
            box.show()
            label = Gtk.Label('Nota {}'.format(n))
            label.set_justify(Gtk.Justification.LEFT)

            box.add(label)
            box.add(Gtk.Label(repr(datetime.now())))

            row = Gtk.ListBoxRow()
            row.add(box)
            row.show()

            self.widget.add(row)

        self.widget.show_all()