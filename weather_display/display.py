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
