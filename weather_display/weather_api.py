# src/weather_display/weather_api.py

import requests
from config import (
    DEFAULT_PARAMETER_ID,
    DEFAULT_STATION_ID,
    DEFAULT_PERIOD,
    DATA_URL_TEMPLATE,
)

class WeatherAPI:
    def __init__(self, parameter_id=None, station_id=None, period=None):
        self.parameter_id = parameter_id or DEFAULT_PARAMETER_ID
        self.station_id = station_id or DEFAULT_STATION_ID
        self.period = period or DEFAULT_PERIOD

    def _build_data_url(self):
        return DATA_URL_TEMPLATE.format(
            param=self.parameter_id,
            station=self.station_id,
            period=self.period
        )

    def fetch_observations(self):
        """Fetch JSON weather observation data from SMHI."""
        url = self._build_data_url()
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_latest_observation(self):
        """Extract the latest observation value and timestamp."""
        data = self.fetch_observations()
        observations = data.get("value", [])
        if not observations:
            raise ValueError("No observations found.")

        latest = observations[-1]  # Last entry is most recent
        return {
            "timestamp": latest["date"],
            "value": latest["value"],
            "unit": data.get("parameter", {}).get("unit", "unknown"),
            "station": data.get("station", {}).get("name", "Unknown Station"),
            "parameter": data.get("parameter", {}).get("name", "Unknown Parameter")
        }
