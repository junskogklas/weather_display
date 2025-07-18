# src/weather_display/display.py

from rich.console import Console
from datetime import datetime
import tkinter as tk
from datetime import datetime
import tkinter as tk

console = Console()

# For terminal output
def show_observation(data: dict):
    print(f"\nWeather at Station {data['station']}")
    print(f"Time:        {data['time']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Rain:        {data['rain']}")
    #print(f"Wind Speed:  {data['wind_speed']} m/s")

def show_forecast(forecast_data):
    print("\n📅 Forecast:")
    for day in forecast_data:
        symbol = "🌧️" if day["total_rain"] > 0 else "☀️"
        print(f"{day['day_name']} {day['date']}: {day['max_temp']} °C max, {day['total_rain']} mm {symbol}")

# For GUI
class WeatherDisplay:
    def __init__(self, observation, forecast, fullscreen=False, refresh_freq=None):
        self.observation = observation
        self.forecast = forecast
        self.refresh_freq = refresh_freq  # in minutes or None
        self.root = tk.Tk()
        self.root.title("Weather Display")
        self.root.geometry("480x320")
        self.root.configure(bg="black")

        self.font_title = ("Helvetica", 18, "bold")
        self.font_section = ("Helvetica", 14, "bold")
        self.font_text = ("Helvetica", 12)
        self.font_small = ("Helvetica", 9)

        if fullscreen:
            self.root.attributes('-fullscreen', True)
            self.root.configure(cursor="none")  # Hide cursor
            self.root.bind("<q>", lambda e: self.root.destroy())  # exit with q

        self.build_ui()

    def build_ui(self):
        # Clear previous widgets if any (helpful for refresh)
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title
        title = tk.Label(self.root, text="Weather Report", font=self.font_title,
                         fg="white", bg="black")
        title.pack(pady=(10, 5))

        # Top right: refresh info (if any)
        if self.refresh_freq is not None:
            now_str = datetime.now().strftime("%H:%M:%S")
            freq_text = f"Refreshing every: {self.refresh_freq} min"
            refresh_text = f"Last update: {now_str}"
            top_frame = tk.Frame(self.root, bg="black")
            top_frame.pack(fill="x", padx=10)
            tk.Label(top_frame, text=freq_text, font=self.font_small, fg="grey", bg="black").pack(side="right", anchor="ne")
            tk.Label(top_frame, text=refresh_text, font=self.font_small, fg="grey", bg="black").pack(side="right", anchor="ne", padx=(0,10))

        # Current weather section
        self._add_section_label("Current Weather")
        obs = self.observation

        current = tk.Frame(self.root, bg="black")
        current.pack(pady=2)
        self._add_line(current, "Time", obs.get("time", "N/A"))
        self._add_line(current, "Temperature", f"{obs.get('temperature', 'N/A')} °C")
        self._add_line(current, "Rain", obs.get("rain", "N/A"))

        # Forecast section
        self._add_section_label("4-Day Forecast")

        forecast_frame = tk.Frame(self.root, bg="black")
        forecast_frame.pack(pady=(0, 5))

        for day in self.forecast:
            row = tk.Frame(forecast_frame, bg="black")
            row.pack(anchor="w", padx=20)

            date_label = tk.Label(row, text=f"{day['weekday']} {day['date']}",
                                  font=self.font_text, fg="white", bg="black", width=18, anchor="w")
            temp_label = tk.Label(row, text=f"{day['max_temp']} °C", font=self.font_text,
                                  fg="white", bg="black", width=10, anchor="w")
            rain_label = tk.Label(row, text=f"{day['total_rain']} mm", font=self.font_text,
                                  fg="white", bg="black", width=10, anchor="w")

            date_label.pack(side="left")
            temp_label.pack(side="left")
            rain_label.pack(side="left")

    def _add_section_label(self, text):
        label = tk.Label(self.root, text=text, font=self.font_section,
                         fg="white", bg="black", anchor="w", padx=20)
        label.pack(anchor="w", pady=(10, 2))

    def _add_line(self, parent, label_text, value_text):
        line = tk.Frame(parent, bg="black")
        line.pack(anchor="w", padx=20)

        label = tk.Label(line, text=f"{label_text}: ", font=self.font_text,
                         fg="white", bg="black", width=14, anchor="w")
        value = tk.Label(line, text=value_text, font=self.font_text,
                         fg="white", bg="black", anchor="w")

        label.pack(side="left")
        value.pack(side="left")

    def run(self):
        self.root.mainloop()



