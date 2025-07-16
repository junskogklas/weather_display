# src/weather_display/display.py

from rich.console import Console
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

