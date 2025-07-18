
from weather_api import WeatherAPI
from display import WeatherDisplay
from datetime import datetime

def main():
    api = WeatherAPI()
    observation = api.get_latest_observation()
    forecast = api.get_forecast(days=4)

    for day in forecast:
        dt = datetime.strptime(day["date"], "%Y-%m-%d")
        day["weekday"] = dt.strftime("%a").upper()  # MON, TUE, etc.

    display = WeatherDisplay(observation, forecast)
    display.run()

if __name__ == "__main__":
    main()
