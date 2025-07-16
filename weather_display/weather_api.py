# src/weather_display/weather_api.py

import requests

from config import (
    API_BASE,
    DEFAULT_PARAMETER_ID,
    DEFAULT_STATION_ID,
    DEFAULT_PERIOD,
    FORECAST_URL,
    DEFAULT_COORDS
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
    
    def get_forecast(self, days=6):
        url = FORECAST_URL.format(
            lon=self.lon if hasattr(self, 'lon') else DEFAULT_COORDS["lon"],
            lat=self.lat if hasattr(self, 'lat') else DEFAULT_COORDS["lat"]
        )
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        ts = data.get("timeSeries", [])

        daily_data = {}

        print(url)

        for entry in ts:
            dt = datetime.fromisoformat(entry["validTime"].replace("Z", ""))
            day = dt.date().isoformat()

            if day < datetime.utcnow().date().isoformat():
                continue

            params = {p["name"]: p["values"][0] for p in entry["parameters"]}
            temp = params.get("t")
            rain = params.get("pmean", 0.0) or 0.0

            if temp is not None:
                if day not in daily_data:
                    daily_data[day] = {"temps": [], "rain": 0.0}
                daily_data[day]["temps"].append(temp)
                daily_data[day]["rain"] += rain
        
        print(enumerate(daily_data.items()))

        forecast_summary = []
        for i, (day, data) in enumerate(sorted(daily_data.items())):
            if i >= days:
                break
            max_temp = max(data["temps"])
            total_rain = round(data["rain"], 1)
            dt = datetime.strptime(day, "%Y-%m-%d")
            day_name = dt.strftime("%A")  # Full weekday name

            forecast_summary.append({
                "date": day,
                "day_name": day_name,
                "max_temp": round(max_temp, 1),
                "total_rain": total_rain
            })

        return forecast_summary