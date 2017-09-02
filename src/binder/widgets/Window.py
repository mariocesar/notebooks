import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Window(Gtk.ApplicationWindow):
    def __init__(self, app: Gtk.Application, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.set_default_size(860, 520)

        headerbar = self.app.get_object("headerbar")
        pane = self.app.get_object("pane")
        menu_button = self.app.get_object("menu_button")
        search_button = self.app.get_object("search_button")

        menu_button.set_image(Gtk.Image.new_from_icon_name("open-menu", Gtk.IconSize.LARGE_TOOLBAR))
        search_button.set_image(Gtk.Image.new_from_icon_name("edit-find-symbolic", Gtk.IconSize.LARGE_TOOLBAR))

        self.set_titlebar(headerbar)
        self.add(pane)
        self.show_all()
