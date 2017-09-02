import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Granite


class Headerbar(Gtk.HeaderBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        mode_button = Granite.WidgetsModeButton()
        mode_button.append_text('View')
        mode_button.append_text('Edit')
        mode_button.set_valign(Gtk.Align.CENTER)
        mode_button.set_tooltip_text("Change mode")

        menu = Gtk.Menu()
        menu.add(Gtk.MenuItem.new_with_label("New notebook"))
        menu.add(Gtk.MenuItem.new_with_label("Preferences"))
        menu.add(Gtk.MenuItem.new_with_label("Export"))
        menu.add(Gtk.SeparatorMenuItem())

        button = Gtk.MenuButton()
        button.set_popup(menu)
        button.set_image(Gtk.Image.new_from_icon_name("open-menu", Gtk.IconSize.LARGE_TOOLBAR))

        search_box = Gtk.Box(Gtk.Orientation.HORIZONTAL, 0)

        search_entry = Gtk.SearchEntry()
        search_entry.set_editable(True)
        search_entry.set_visibility(True)
        search_entry.set_vexpand(True)
        search_entry.set_hexpand(True)
        search_entry.set_margin_right(12)
        search_entry.set_max_width_chars(30)

        search_entry_revealer = Gtk.Revealer()
        search_button_revealer = Gtk.Revealer()
        search_entry_revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_LEFT)
        search_button_revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_LEFT)

        search_button = Gtk.Button.new_from_icon_name("edit-find-symbolic", Gtk.IconSize.LARGE_TOOLBAR)
        search_button.set_tooltip_text("Search your current notebook")

        search_button_revealer.add(search_button)
        search_entry_revealer.add(search_entry)

        search_entry_revealer.set_reveal_child(False)
        search_button_revealer.set_reveal_child(True)

        menu.show_all()

        self.set_title("Note Binder")
        self.set_show_close_button(True)
        self.pack_start(mode_button)
        self.pack_end(button)

        search_box.add(search_button_revealer)
        search_box.add(search_entry_revealer)

        self.pack_end(search_box)
        self.show_all()
