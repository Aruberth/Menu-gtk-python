import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio
from ui.main_window import MainWindow

class App(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id = "org.simple.python.menu",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )

    def do_activate(self):
        window = MainWindow(self)
        window.present()
