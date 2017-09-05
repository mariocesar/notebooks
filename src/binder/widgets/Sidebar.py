import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject


class Item(GObject.GObject):
    parent = GObject.Property(type=object, default=None)

    def __init__(self, name):
        self.name = name

class ExpandableItem(GObject.GObject):
    __gsignals__ = {
        'child_added': (GObject.SIGNAL_RUN_FIRST, None, (Item,)),
        'child_removed': (GObject.SIGNAL_RUN_FIRST, None, (Item,)),
        'toggled': (GObject.SIGNAL_RUN_FIRST, None, (Item,)),
    }

    def __init__(self, name):
        self.name = name

    def add(self, item):
        item.parent = self
        self.children_list.append(item)
        self.emit('child_added', item)

    def remove(self, item):
        self.children_list.remove(item)
        self.emit('child_removed', item)
        item.parent = None

    def clear(self):
        for children in self.children_list:
            self.remove(children)



class Sidebar(Gtk.ScrolledWindow):
    pass
