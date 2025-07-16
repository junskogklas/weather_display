# src/weather_display/weather_api.py

import requests

from config import (
    API_BASE,
    DEFAULT_PARAMETER_ID,
    DEFAULT_STATION_ID,
    DEFAULT_PERIOD,
    DATA_URL_TEMPLATE,
)
from datetime import datetime

class WeatherAPI:
    def __init__(self, parameter_id=None, station_id=None, period=None):
        self.parameter_id = parameter_id or DEFAULT_PARAMETER_ID
        self.station_id = station_id or DEFAULT_STATION_ID
        self.period = period or DEFAULT_PERIOD

    def fetch_parameter_value(self, station_id, parameter_id, period="latest-hour"):
        url = f"{API_BASE}/version/latest/parameter/{parameter_id}/station/{station_id}/period/{period}/data.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        values = data.get("value", [])
        if not values:
            return None, None

        latest = values[-1]
        timestamp = latest["date"]
        value = latest["value"]
        return timestamp, value


    def interpret_rain(self, mm):

        try:
            mm = float(mm)
        except (ValueError, TypeError):
            return "Unknown"
        
        if mm is None:
            return "Unknown"
        if mm == 0:
            return "No rain"
        elif mm < 1:
            return f"Light rain ({mm} mm)"
        elif mm < 5:
            return f"Moderate rain ({mm} mm)"
        else:
            return f"Heavy rain ({mm} mm)"


    def get_latest_observation(self):
        param_temp = 1
        param_rain_mm = 14
        # ignoring for now
        # param_wind_speed = 4
        temp_ts, temperature = self.fetch_parameter_value(self.station_id, param_temp)
        _, rain_mm = self.fetch_parameter_value(self.station_id, param_rain_mm)

        return {
            "station": self.station_id,
            "time": datetime.fromtimestamp(temp_ts / 1000).strftime("%Y-%m-%d %H:%M"),
            "temperature": temperature,
            "rain": self.interpret_rain(rain_mm)
        }