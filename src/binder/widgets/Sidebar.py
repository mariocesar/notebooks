from gi.repository import Gtk


class Sidebar(Gtk.PlacesSidebar):
    def __init__(self):
        super(Sidebar, self).__init__()