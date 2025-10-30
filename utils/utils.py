from datetime import datetime
import locale
import subprocess
from pydbus import SystemBus
from os import environ
import psutil


locale.setlocale(locale.LC_TIME, 'C')  # 'C' é o locale padrão em inglês neutro

class Utils:
    def get_hour(widget):
        widget.set_text(f"{datetime.now().hour:02}")
        return True

    def get_minutes(widget):
        widget.set_text(f"{datetime.now().minute:02}")
        return True

    def get_date(widget):
        date = datetime.now()
        string = f"{date.strftime('%B')} {date.day}, {date.year}".capitalize()
        widget.set_text(string)
        return True

    def changue_volume(widget):
        value = widget.get_value()
        subprocess.Popen(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{value}%"])

    def changue_microphone(widget):
        value = widget.get_value()
        subprocess.Popen(["pactl", "set-source-volume", "@DEFAULT_SOURCE@", f"{value}%"])

    def changue_brightness(widget):
        value = widget.get_value()
        subprocess.Popen(["brightnessctl", "s", f"{value}%"])

    def state_wifi(widget):
        nm = SystemBus().get("org.freedesktop.NetworkManager")

        if widget.get_active():
            nm.WirelessEnabled = True
        else:
            nm.WirelessEnabled = False

    def state_bluetooth(widget):
        if widget.get_active():
            subprocess.Popen("bluetoothctl power on".split())
        else:
            subprocess.Popen("bluetoothctl power off".split())

    def show_notifications(widget):
        subprocess.Popen("swaync-client -t".split())

    def state_blue_filter(widget):
        if widget.get_active():
            subprocess.Popen("hyprsunset")
        else:
            subprocess.Popen("killall hyprsunset".split())

    def state_ultra_economy(widget):
        if widget.get_active():
            subprocess.Popen("powerprofilesctl set power-saver".split())
        else:
            subprocess.Popen("powerprofilesctl set balanced".split())

    def state_theme(widget):
        if widget.get_active():
            subprocess.Popen('gsettings set org.gnome.desktop.interface color-scheme "prefer-dark"'.split())
        else:
            subprocess.Popen('gsettings set org.gnome.desktop.interface color-scheme "prefer-light"'.split())

    def show_logout(widget):
        subprocess.Popen("wlogout")

    def show_hypr_conf(widget):
        user = environ.get('USER')
        subprocess.Popen(f"code /home/{user}/.config/hypr/hyprland.conf".split())

    def update_cpu_status(usage, number_usage, temperature, number_temperature):
        cpu_usage = psutil.cpu_percent(interval=None);
        temperature_cpu = list(psutil.sensors_temperatures()["k10temp"][0])[1]

        usage.set_fraction(cpu_usage / 100)
        number_usage.set_text(f"{cpu_usage}%")
        temperature.set_fraction(temperature_cpu / 100)
        number_temperature.set_text(f"{temperature_cpu}°C")

        return True

    def update_ram_status(usage, label_number_temperature, freeMemory):
        ram_data = list(psutil.virtual_memory())
        ram_usage = ram_data[2]
        ram_free = str(ram_data[1])[:4]

        usage.set_fraction(ram_usage / 100)
        label_number_temperature.set_text(f"{ram_usage}%")
        freeMemory.set_text(f"{ram_free} MB")
        return True

    def update_gpu_status(usage, label_usage, temperature, label_temperature):
        gpu_data = subprocess.check_output("nvidia-smi --query-gpu=utilization.gpu,temperature.gpu --format=csv,noheader,nounits".split(), text=True)
        gpu_usage = float(gpu_data[:2].replace(",", ""))
        gpu_temperature = float(gpu_data[-3:])

        usage.set_fraction(gpu_usage / 100)
        label_usage.set_text(str(f"{gpu_usage}%"))
        temperature.set_fraction(gpu_temperature / 100)
        label_temperature.set_text(f"{gpu_temperature}°C")
        return True
