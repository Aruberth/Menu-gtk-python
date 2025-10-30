from gi.repository import Gtk, Gdk, GLib

class Utils_Task:
    def __init__ (self, card_task, parent_widget, db):
        self.card_task = card_task
        self.parent_widget = parent_widget
        self.db = db

        self.load_tasks()

    def add_task(self, id, title, description):

        task_checkBox = Gtk.CheckButton()
        task_checkBox.set_css_classes(["task_checkBox"])
        task_checkBox.id = id
        task_checkBox.connect("toggled", lambda btn: self.close_task(btn))

        task_tittle = Gtk.Label(label=title)
        task_tittle.set_xalign(0.0)
        task_tittle.set_css_classes(["task_tittle"])

        task_description = Gtk.Label(label=description)
        task_description.set_xalign(0.0)
        task_description.set_css_classes(["task_description"])

        task_informations = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        task_informations.set_css_classes(["task_informations"])
        task_informations.append(task_tittle)
        task_informations.append(task_description)

        task = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        task.set_css_classes(["task_space"])
        task.set_margin_start(10)
        task.append(task_checkBox)
        task.append(task_informations)

        self.card_task.append(task)

    def load_tasks(self):
        child = self.card_task.get_first_child().get_next_sibling()
        while child is not None:
            next_child = child.get_next_sibling()
            self.card_task.remove(child)
            child = next_child

        for task in self.db.show_tasks():
            self.add_task(task[0], task[1], task[2])

    def close_task(self, check_button):
        self.db.close_task(check_button.id)
        self.load_tasks()

    def open_popup(self, btn):
        label_title = Gtk.Label(label="Title")
        entry_title = Gtk.Entry()

        label_description = Gtk.Label(label="Description")
        entry_description = Gtk.Entry()

        button_create_task = Gtk.Button(label="Add task")

        def create_task(button):
            self.db.create_task(entry_title.get_text(), entry_description.get_text())
            popover_add_task.popdown()
            self.load_tasks()

        button_create_task.connect("clicked", create_task)
        button_create_task.set_css_classes(["button_create_task"])

        popover_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        popover_box.append(label_title)
        popover_box.append(entry_title)
        popover_box.append(label_description)
        popover_box.append(entry_description)
        popover_box.append(button_create_task)

        popover_add_task = Gtk.Popover()
        popover_add_task.set_css_classes(["popover_box"])
        popover_add_task.set_child(popover_box)
        popover_add_task.set_parent(self.parent_widget)

        rect = Gdk.Rectangle()
        rect.x = 0
        rect.y = 0
        rect.width = self.parent_widget.get_allocated_width()
        rect.height = self.parent_widget.get_allocated_height()
        popover_add_task.set_pointing_to(rect)

        popover_add_task.popup()
