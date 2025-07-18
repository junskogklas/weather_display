# src/weather_display/display.py

from rich.console import Console
from datetime import datetime
import tkinter as tk
from datetime import datetime

console = Console()

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

class WeatherDisplay:
    def __init__(self, observation, forecast):
        self.observation = observation
        self.forecast = forecast
        self.root = tk.Tk()
        self.root.title("Weather Terminal")
        self.root.geometry("480x320")
        self.root.configure(bg="black")
        self.font = ("Courier", 12)
        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(self.root, text="=== WEATHER MONITOR ===", font=("Courier", 14, "bold"),
                 fg="green", bg="black").pack(anchor="w", padx=10, pady=5)

        # Current Weather
        obs = self.observation
        now_lines = [
            f"TIME         : {obs.get('time', 'N/A')}",
            f"TEMPERATURE  : {obs.get('temperature', 'N/A')} °C",
            f"RAIN STATUS  : {obs.get('rain', 'N/A')}",
        ]

        for line in now_lines:
            tk.Label(self.root, text=line, font=self.font, fg="white", bg="black").pack(anchor="w", padx=10)

        # Spacer
        tk.Label(self.root, text="", bg="black").pack()

        # Forecast Section
        tk.Label(self.root, text="=== FORECAST (NEXT DAYS) ===",
                 font=("Courier", 14, "bold"), fg="green", bg="black").pack(anchor="w", padx=10)

        for day in self.forecast:
            line = f"{day['weekday']} {day['date']} - MAX: {day['max_temp']}°C | RAIN: {day['total_rain']} mm"
            tk.Label(self.root, text=line, font=self.font, fg="white", bg="black").pack(anchor="w", padx=10)

    def run(self):
        self.root.mainloop()



