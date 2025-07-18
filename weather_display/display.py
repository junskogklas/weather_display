# src/weather_display/display.py

from rich.console import Console
from datetime import datetime
import tkinter as tk

console = Console()

def show_observation(data: dict):
    print(f"\nWeather at Station {data['station']}")
    print(f"Time:        {data['time']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Rain:        {data['rain']}")

def show_forecast(forecast_data):
    print("\n📅 Forecast:")
    for day in forecast_data:
        symbol = "🌧️" if day["total_rain"] > 0 else "☀️"
        print(f"{day['day_name']} {day['date']}: {day['max_temp']} °C max, {day['total_rain']} mm {symbol}")

class WeatherDisplay:
    def __init__(self, observation, forecast, fullscreen=False, refresh_freq=None):
        self.observation = observation
        self.forecast = forecast
        self.refresh_freq = refresh_freq
        self.root = tk.Tk()
        self.root.title("Weather Display")

        if fullscreen:
            self.root.attributes('-fullscreen', True)
            self.root.configure(cursor="none")
            self.root.bind("<q>", lambda e: self.root.destroy())
        else:
            self.root.geometry("1024x600")

        self.root.configure(bg="black")

        # Fonts
        self.font_title = ("Helvetica", 24, "bold")
        self.font_section = ("Helvetica", 18, "bold")
        self.font_text = ("Helvetica", 14)
        self.font_small = ("Helvetica", 10)

        self.build_ui()

    def build_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # === Top bar (title and refresh) ===
        topbar = tk.Frame(self.root, bg="black")
        topbar.pack(fill="x", pady=(10, 0))
        tk.Label(topbar, text="Weather Report", font=self.font_title, fg="white", bg="black").pack(side="left", padx=30)

        if self.refresh_freq is not None:
            now_str = datetime.now().strftime("%H:%M:%S")
            right = tk.Frame(topbar, bg="black")
            right.pack(side="right", padx=30)
            tk.Label(right, text=f"Last update: {now_str}", font=self.font_small,
                     fg="grey", bg="black").pack(anchor="e")
            tk.Label(right, text=f"Refreshing every: {self.refresh_freq} min", font=self.font_small,
                     fg="grey", bg="black").pack(anchor="e")

        # === Top section: Today ===
        top_section = tk.Frame(self.root, bg="black")
        top_section.pack(expand=True, fill="both", padx=30, pady=5)

        # Subtitles
        labels = tk.Frame(top_section, bg="black")
        labels.pack(fill="x")
        tk.Label(labels, text="Current Weather", font=self.font_section, fg="white", bg="black").pack(side="left", expand=True)
        tk.Label(labels, text="Today's Forecast", font=self.font_section, fg="white", bg="black").pack(side="left", expand=True)

        # Data columns
        cols = tk.Frame(top_section, bg="black")
        cols.pack(fill="both", expand=True)

        left = tk.Frame(cols, bg="black")
        left.pack(side="left", expand=True, fill="both")
        obs = self.observation
        self._add_line(left, "Time", obs.get("time", "N/A"))
        self._add_line(left, "Temperature", f"{obs.get('temperature', 'N/A')} °C")
        self._add_line(left, "Rain", obs.get("rain", "N/A"))

        right = tk.Frame(cols, bg="black")
        right.pack(side="left", expand=True, fill="both")
        today = self.forecast[0] if self.forecast else {}
        self._add_line(right, "Max Temp", f"{today.get('max_temp', 'N/A')} °C")
        self._add_line(right, "Rain", f"{today.get('total_rain', 'N/A')} mm")

        # === Bottom section: 3-Day Forecast ===
        self._add_section_label("Next 3 Days")

        bottom = tk.Frame(self.root, bg="black")
        bottom.pack(expand=True, fill="both", padx=30, pady=(0, 20))

        days_frame = tk.Frame(bottom, bg="black")
        days_frame.pack(expand=True, fill="both")

        for day in self.forecast[1:4]:
            day_frame = tk.Frame(days_frame, bg="black")
            day_frame.pack(side="left", expand=True, fill="both", padx=10)

            tk.Label(day_frame, text=f"{day['weekday']} {day['date']}", font=self.font_text,
                     fg="white", bg="black").pack(pady=5)
            tk.Label(day_frame, text=f"{day['max_temp']} °C", font=self.font_text,
                     fg="white", bg="black").pack(pady=5)
            tk.Label(day_frame, text=f"{day['total_rain']} mm", font=self.font_text,
                     fg="white", bg="black").pack(pady=5)

    def _add_section_label(self, text):
        tk.Label(self.root, text=text, font=self.font_section,
                 fg="white", bg="black", anchor="w", padx=30).pack(anchor="w", pady=(10, 2))

    def _add_line(self, parent, label_text, value_text):
        line = tk.Frame(parent, bg="black")
        line.pack(anchor="w", pady=2)

        tk.Label(line, text=f"{label_text}: ", font=self.font_text,
                 fg="white", bg="black", width=16, anchor="w").pack(side="left")
        tk.Label(line, text=value_text, font=self.font_text,
                 fg="white", bg="black", anchor="w").pack(side="left")

    def run(self):
        self.root.mainloop()
