# src/weather_display/display.py

from rich.console import Console
from datetime import datetime

console = Console()

def show_observation(observation: dict):
    timestamp_unix = observation["timestamp"] / 1000  # Convert ms to s
    time_str = datetime.fromtimestamp(timestamp_unix).strftime("%Y-%m-%d %H:%M")

    console.print(f"\n[bold cyan]Current Observation from {observation['station']}[/bold cyan]")
    console.print(f"Parameter: {observation['parameter']}")
    console.print(f"Time: {time_str}")
    console.print(f"Value: [bold yellow]{observation['value']} {observation['unit']}[/bold yellow]")
