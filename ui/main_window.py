from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
from utils.utils import Utils
from utils.utils_task import Utils_Task
from utils.tasks import Database


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Simple_Menu")
        self.set_default_size(1920, 1080)

        #----------IMPORT CSS STYLES----------#
        css = Gtk.CssProvider()
        css.load_from_path('ui/styles.css')

        display = Gdk.Display.get_default()
        Gtk.StyleContext.add_provider_for_display(
            display,
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        #----------CREATE TIME CARD----------#
        hours = Gtk.Label(label="...")
        minutes = Gtk.Label(label="...")

        GLib.timeout_add_seconds(1, Utils.get_hour, hours)
        GLib.timeout_add_seconds(1, Utils.get_minutes, minutes)
        Utils.get_hour
        Utils.get_minutes

        time = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        time.set_css_classes(['time_card_hours'])
        time.set_size_request(270, 370)
        time.append(hours)
        time.append(minutes)

        date = Gtk.Label(label="...")
        date.set_css_classes(['time_card_date'])

        GLib.timeout_add_seconds(1, Utils.get_date, date)
        Utils.get_date

        time_space = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=80)
        time_space.set_halign(Gtk.Align.CENTER)
        time_space.set_valign(Gtk.Align.CENTER)
        time_space.append(time)
        time_space.append(date)

        time_card = Gtk.Frame()
        time_card.set_child(time_space)
        time_card.set_css_classes(["time_card"])

        #----------CREATE SLIDERS----------# #MELHORAR APÓS INTEGRAÇÃO DO BACKEND#
        volume_adjustment = Gtk.Adjustment(value=50, lower=0, upper=100, step_increment=1)
        volume = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=volume_adjustment)
        volume.set_css_classes(["sliders"])
        volume.set_inverted(True)
        volume.connect("value-changed", Utils.changue_volume)

        svg_volume = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/volume.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_volume = Gtk.Image.new_from_pixbuf(svg_volume)
        icon_volume.set_pixel_size(80)
        icon_volume.set_can_target(False)
        icon_volume.set_sensitive(False)
        icon_volume.set_halign(Gtk.Align.CENTER)
        icon_volume.set_valign(Gtk.Align.END)
        icon_volume.set_margin_bottom(50)
        icon_volume.set_margin_start(10)

        volume_overlay = Gtk.Overlay()
        volume_overlay.set_child(volume)
        volume_overlay.add_overlay(icon_volume)

        volume_box = Gtk.Box()
        time.set_size_request(100, 420)
        volume_box.append(volume_overlay)

        microphone_adjustment = Gtk.Adjustment(value=35, lower=0, upper=40, step_increment=1)
        microphone = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=microphone_adjustment)
        microphone.set_css_classes(["sliders"])
        microphone.set_inverted(True)
        microphone.connect("value-changed", Utils.changue_microphone)

        svg_microphone = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/microphone.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_microphone = Gtk.Image.new_from_pixbuf(svg_microphone)
        icon_microphone.set_pixel_size(80)
        icon_microphone.set_can_target(False)
        icon_microphone.set_sensitive(False)
        icon_microphone.set_halign(Gtk.Align.CENTER)
        icon_microphone.set_valign(Gtk.Align.END)
        icon_microphone.set_margin_bottom(50)

        microphone_overlay = Gtk.Overlay()
        microphone_overlay.set_child(microphone)
        microphone_overlay.add_overlay(icon_microphone)

        microphone_box = Gtk.Box()
        time.set_size_request(100, 420)
        microphone_box.append(microphone_overlay)

        brightness_adjustment = Gtk.Adjustment(value=50, lower=0, upper=100, step_increment=1)
        brightness = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=brightness_adjustment)
        brightness.set_css_classes(["sliders"])
        brightness.set_inverted(True)
        brightness.connect("value-changed", Utils.changue_brightness)

        svg_brightness = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/brightness.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_brightness = Gtk.Image.new_from_pixbuf(svg_brightness)
        icon_brightness.set_pixel_size(80)
        icon_brightness.set_can_target(False)
        icon_brightness.set_sensitive(False)
        icon_brightness.set_halign(Gtk.Align.CENTER)
        icon_brightness.set_valign(Gtk.Align.END)
        icon_brightness.set_margin_bottom(50)

        brightness_overlay = Gtk.Overlay()
        brightness_overlay.set_child(brightness)
        brightness_overlay.add_overlay(icon_brightness)

        brightness_box = Gtk.Box()
        time.set_size_request(100, 420)
        brightness_box.append(brightness_overlay)

        sliders_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        for widget in [volume_box, microphone_box, brightness_box]:
            sliders_box.append(widget)

        #----------CREATE BUTTONS----------#

        button_wifi = Gtk.ToggleButton()
        button_wifi.set_size_request(100, 100)
        button_wifi.set_css_classes(["button"])
        button_wifi.connect("toggled", Utils.state_wifi)

        svg_wifi = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/wifi.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_wifi = Gtk.Image.new_from_pixbuf(svg_wifi)
        icon_wifi.set_pixel_size(80)
        icon_wifi.set_can_target(False)
        icon_wifi.set_sensitive(False)
        icon_wifi.set_halign(Gtk.Align.CENTER)
        icon_wifi.set_valign(Gtk.Align.CENTER)

        wifi_overlay = Gtk.Overlay()
        wifi_overlay.set_child(button_wifi)
        wifi_overlay.add_overlay(icon_wifi)

        button_bluetooth = Gtk.ToggleButton()
        button_bluetooth.set_size_request(100, 100)
        button_bluetooth.set_css_classes(["button"])
        button_bluetooth.connect("toggled", Utils.state_bluetooth)

        svg_bluetooth = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/bluetooth.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_bluetooth = Gtk.Image.new_from_pixbuf(svg_bluetooth)
        icon_bluetooth.set_pixel_size(80)
        icon_bluetooth.set_can_target(False)
        icon_bluetooth.set_sensitive(False)
        icon_bluetooth.set_halign(Gtk.Align.CENTER)
        icon_bluetooth.set_valign(Gtk.Align.CENTER)

        bluetooth_overlay = Gtk.Overlay()
        bluetooth_overlay.set_child(button_bluetooth)
        bluetooth_overlay.add_overlay(icon_bluetooth)

        button_notifications = Gtk.Button()
        button_notifications.set_size_request(100, 100)
        button_notifications.set_css_classes(["button"])
        button_notifications.connect("clicked", Utils.show_notifications)

        svg_notifications = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/notifications.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_notifications = Gtk.Image.new_from_pixbuf(svg_notifications)
        icon_notifications.set_pixel_size(80)
        icon_notifications.set_can_target(False)
        icon_notifications.set_sensitive(False)
        icon_notifications.set_halign(Gtk.Align.CENTER)
        icon_notifications.set_valign(Gtk.Align.CENTER)

        notifications_overlay = Gtk.Overlay()
        notifications_overlay.set_child(button_notifications)
        notifications_overlay.add_overlay(icon_notifications)

        button_blue_filter = Gtk.ToggleButton()
        button_blue_filter.set_size_request(100, 100)
        button_blue_filter.set_css_classes(["button"])
        button_blue_filter.connect("toggled", Utils.state_blue_filter)

        svg_blue_filter = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/blue_filter.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_blue_filter = Gtk.Image.new_from_pixbuf(svg_blue_filter)
        icon_blue_filter.set_pixel_size(80)
        icon_blue_filter.set_can_target(False)
        icon_blue_filter.set_sensitive(False)
        icon_blue_filter.set_halign(Gtk.Align.CENTER)
        icon_blue_filter.set_valign(Gtk.Align.CENTER)

        blue_filter_overlay = Gtk.Overlay()
        blue_filter_overlay.set_child(button_blue_filter)
        blue_filter_overlay.add_overlay(icon_blue_filter)

        button_ultra_economy = Gtk.ToggleButton()
        button_ultra_economy.set_size_request(100, 100)
        button_ultra_economy.set_css_classes(["button"])
        button_ultra_economy.connect("toggled", Utils.state_ultra_economy)

        svg_ultra_economy = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/ultra_economy.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_ultra_economy = Gtk.Image.new_from_pixbuf(svg_ultra_economy)
        icon_ultra_economy.set_pixel_size(80)
        icon_ultra_economy.set_can_target(False)
        icon_ultra_economy.set_sensitive(False)
        icon_ultra_economy.set_halign(Gtk.Align.CENTER)
        icon_ultra_economy.set_valign(Gtk.Align.CENTER)

        ultra_economy_overlay = Gtk.Overlay()
        ultra_economy_overlay.set_child(button_ultra_economy)
        ultra_economy_overlay.add_overlay(icon_ultra_economy)

        button_theme = Gtk.ToggleButton()
        button_theme.set_size_request(100, 100)
        button_theme.set_css_classes(["button"])
        button_theme.connect("toggled", Utils.state_theme)

        svg_theme = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/theme.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_theme = Gtk.Image.new_from_pixbuf(svg_theme)
        icon_theme.set_pixel_size(80)
        icon_theme.set_can_target(False)
        icon_theme.set_sensitive(False)
        icon_theme.set_halign(Gtk.Align.CENTER)
        icon_theme.set_valign(Gtk.Align.CENTER)

        theme_overlay = Gtk.Overlay()
        theme_overlay.set_child(button_theme)
        theme_overlay.add_overlay(icon_theme)

        button_power = Gtk.ToggleButton()
        button_power.set_size_request(100, 100)
        button_power.set_css_classes(["button"])
        button_power.connect("toggled", Utils.show_logout)

        svg_power = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/power.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_power = Gtk.Image.new_from_pixbuf(svg_power)
        icon_power.set_pixel_size(80)
        icon_power.set_can_target(False)
        icon_power.set_sensitive(False)
        icon_power.set_halign(Gtk.Align.CENTER)
        icon_power.set_valign(Gtk.Align.CENTER)

        power_overlay = Gtk.Overlay()
        power_overlay.set_child(button_power)
        power_overlay.add_overlay(icon_power)

        button_wallpaper = Gtk.ToggleButton()
        button_wallpaper.set_size_request(100, 100)
        button_wallpaper.set_css_classes(["button"])
        #button_wallpaper.connect("toggled", Utils.state_wallpaper)

        svg_wallpaper = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "assets/wallpaper.svg",
            width=80,
            height=80,
            preserve_aspect_ratio=False
        )
        icon_wallpaper = Gtk.Image.new_from_pixbuf(svg_wallpaper)
        icon_wallpaper.set_pixel_size(80)
        icon_wallpaper.set_can_target(False)
        icon_wallpaper.set_sensitive(False)
        icon_wallpaper.set_halign(Gtk.Align.CENTER)
        icon_wallpaper.set_valign(Gtk.Align.CENTER)

        wallpaper_overlay = Gtk.Overlay()
        wallpaper_overlay.set_child(button_wallpaper)
        wallpaper_overlay.add_overlay(icon_wallpaper)

        #VERSAO REDUZIDA, APLICAR PARA O RESTANTE
        button_conf = Gtk.ToggleButton()
        button_conf.set_size_request(100, 100)
        button_conf.set_css_classes(["button"])
        button_conf.connect("toggled", Utils.show_hypr_conf)
        conf_image = Gtk.Image.new_from_file("assets/conf.svg")
        conf_image.set_pixel_size(80)
        button_conf.set_child(conf_image)

        buttons_grid = Gtk.Grid()
        buttons_grid.set_column_spacing(40)
        buttons_grid.set_row_spacing(60)
        buttons_grid.set_valign(Gtk.Align.END)
        buttons_grid.set_vexpand(True)

        buttons = [wifi_overlay, bluetooth_overlay, notifications_overlay,
                   blue_filter_overlay, ultra_economy_overlay, theme_overlay,
                   power_overlay, wallpaper_overlay, button_conf]
        for index in range(len(buttons)):
            buttons_grid.attach(buttons[index], index % 3, index // 3, 1, 1)

        box_button_grid = Gtk.Box()
        box_button_grid.append(buttons_grid)
        box_button_grid.set_css_classes(["box_button_grid"])

        #----------CREATE TASKS CARD----------#
        task_label = Gtk.Label(label="TASKS")
        task_label.set_css_classes(["task_label_tittle"])

        card_task = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        card_task.set_css_classes(["card_task"])
        card_task.append(task_label)

        button_add_task = Gtk.Button()
        button_add_task.set_halign(Gtk.Align.END)
        button_add_task.set_valign(Gtk.Align.START)
        button_add_task.set_margin_top(10)
        button_add_task.set_margin_end(10)
        button_add_task.set_css_classes(["button_add_task"])
        img = Gtk.Image.new_from_file("assets/plus.svg")
        img.set_pixel_size(20)
        button_add_task.set_child(img)

        utils_tasks = Utils_Task(card_task, button_add_task, Database())

        button_add_task.connect("clicked", lambda btn: utils_tasks.open_popup(btn))

        overlay_task = Gtk.Overlay()
        overlay_task.set_child(card_task)
        overlay_task.add_overlay(button_add_task)

        #----------CREATE CPU STATUS----------#
        label_cpu = Gtk.Label(label="CPU")
        label_cpu.set_css_classes(["label_status_tittle"])
        label_usage_cpu = Gtk.Label(label="USAGE")
        label_usage_cpu.set_css_classes(["label_internal"])
        progress_usage_cpu = Gtk.ProgressBar()
        progress_usage_cpu.set_css_classes(["progress_status_usage"])

        label_number_cpu = Gtk.Label(label="...")
        label_number_cpu.set_css_classes(["label_status"])
        overlay_usage_cpu = Gtk.Overlay()
        overlay_usage_cpu.set_child(progress_usage_cpu)
        overlay_usage_cpu.add_overlay(label_number_cpu)

        label_temperature = Gtk.Label(label="TEMPERATURE")
        label_temperature.set_css_classes(["label_internal"])
        progress_temperature_cpu = Gtk.ProgressBar()
        progress_temperature_cpu.set_css_classes(["progress_status_temperature"])

        label_number_temperature = Gtk.Label(label="...")
        label_number_temperature.set_css_classes(["label_status"])
        overlay_temperature_cpu = Gtk.Overlay()
        overlay_temperature_cpu.set_child(progress_temperature_cpu)
        overlay_temperature_cpu.add_overlay(label_number_temperature)

        GLib.timeout_add_seconds(2, Utils.update_cpu_status, progress_usage_cpu, label_number_cpu, progress_temperature_cpu, label_number_temperature)
        Utils.update_cpu_status

        box_cpu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=7)
        box_cpu.set_css_classes(["box_status"])
        box_cpu.set_size_request(420, 270)

        status_structure = [label_cpu, label_usage_cpu, overlay_usage_cpu,
                            label_temperature, overlay_temperature_cpu]
        for component in status_structure:
            box_cpu.append(component)

        #----------CREATE RAM STATUS----------#
        label_usage_ram = Gtk.Label(label="USAGE")
        label_usage_ram.set_css_classes(["label_internal"])

        label_temperature = Gtk.Label(label="FREE MEMORY")
        label_temperature.set_css_classes(["label_internal"])
        progress_usage_ram = Gtk.ProgressBar()
        progress_usage_ram.set_css_classes(["progress_status_usage"])

        label_number_temperature = Gtk.Label(label="...")
        label_number_temperature.set_css_classes(["label_status"])
        overlay_temperature_ram = Gtk.Overlay()
        overlay_temperature_ram.set_child(progress_usage_ram)
        overlay_temperature_ram.add_overlay(label_number_temperature)

        box_free_ram = Gtk.Frame()
        box_free_ram.set_css_classes(["free_ram"])
        label_free_ram = Gtk.Label()
        label_free_ram.set_css_classes(["label_status"])
        label_free_ram.set_valign(Gtk.Align.CENTER)
        label_free_ram.set_halign(Gtk.Align.CENTER)
        box_free_ram.set_size_request(100, 30)
        box_free_ram.set_child(label_free_ram)

        GLib.timeout_add_seconds(2, Utils.update_ram_status, progress_usage_ram, label_number_temperature, label_free_ram)
        Utils.update_ram_status

        box_ram = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=7)
        box_ram.set_css_classes(["box_status"])
        label_ram = Gtk.Label(label="RAM")
        label_ram.set_css_classes(["label_status_tittle"])
        box_ram.append(label_ram)
        box_ram.append(label_usage_ram)
        box_ram.append(overlay_temperature_ram)
        box_ram.append(label_temperature)
        box_ram.append(box_free_ram)

        box_ram.set_size_request(420, 270)

        #----------CREATE GPU STATUS----------#
        label_usage_gpu = Gtk.Label(label="USAGE")
        label_usage_gpu.set_css_classes(["label_internal"])
        label_temperature = Gtk.Label(label="TEMPERATURE")
        label_temperature.set_css_classes(["label_internal"])
        progress_usage_gpu = Gtk.ProgressBar()
        progress_usage_gpu.set_css_classes(["progress_status_usage"])

        label_number_usage_gpu = Gtk.Label(label="...")
        label_number_usage_gpu.set_css_classes(["label_status"])
        overlay_number_usage_gpu = Gtk.Overlay()
        overlay_number_usage_gpu.set_child(progress_usage_gpu)
        overlay_number_usage_gpu.add_overlay(label_number_usage_gpu)

        progress_temperature_gpu = Gtk.ProgressBar()
        progress_temperature_gpu.set_css_classes(["progress_status_temperature"])

        label_number_temperature_gpu = Gtk.Label(label="...")
        label_number_temperature_gpu.set_css_classes(["label_status"])
        overlay_number_temperature_gpu = Gtk.Overlay()
        overlay_number_temperature_gpu.set_child(progress_temperature_gpu)
        overlay_number_temperature_gpu.add_overlay(label_number_temperature_gpu)

        box_gpu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=7)
        box_gpu.set_css_classes(["box_status"])
        label_gpu = Gtk.Label(label="GPU")
        label_gpu.set_css_classes(["label_status_tittle"])
        box_gpu.append(label_gpu)
        box_gpu.append(label_usage_gpu)
        box_gpu.append(overlay_number_usage_gpu)
        box_gpu.append(label_temperature)
        box_gpu.append(overlay_number_temperature_gpu)
        box_gpu.set_size_request(420, 270)

        GLib.timeout_add_seconds(2, Utils.update_gpu_status, progress_usage_gpu, label_number_usage_gpu, progress_temperature_gpu, label_number_temperature_gpu)
        Utils.update_gpu_status

        card_status = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        card_status.append(box_cpu)
        card_status.append(box_ram)
        card_status.append(box_gpu)
        card_status.set_valign(Gtk.Align.END)

        #----------CHANGE SIZE OF WIDGETS----------#

        time_card.set_size_request(500, 980)

        volume.set_size_request(100, 420)
        microphone.set_size_request(100, 420)
        brightness.set_size_request(100, 420)
        sliders_box.set_size_request(380, 420)

        box_button_grid.set_size_request(380, 420)
        card_task.set_size_request(800, 450)
        card_status.set_size_request(420, 940)

        #----------GRID GLOBAL ORGANIZATION----------#
        grid_global = Gtk.Grid()
        grid_global.set_hexpand(True)
        grid_global.set_vexpand(True)
        grid_global.set_halign(Gtk.Align.FILL)
        grid_global.set_valign(Gtk.Align.FILL)
        grid_global.set_column_spacing(40)
        grid_global.set_row_spacing(60)
        grid_global.set_margin_top(50)
        grid_global.set_margin_bottom(50)
        grid_global.set_margin_start(50)
        grid_global.set_margin_end(50)

        grid_global.attach(time_card, 0, 0, 1, 2)
        grid_global.attach(sliders_box, 1, 0, 1, 1)
        grid_global.attach(box_button_grid,2, 0, 1, 1)
        grid_global.attach(overlay_task, 1, 1, 2, 1)
        grid_global.attach(card_status, 3, 0, 1, 2)

        #----------SET self AS WINDOW----------#
        self.set_child(grid_global)
        self.set_css_classes(["window"])

        #----------SET AUXILIARY FUNCTIONS----------#



