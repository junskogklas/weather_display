# src/weather_display/main.py

from weather_api import WeatherAPI
from display import show_observation, show_forecast

def main():
    api = WeatherAPI()
    obs = api.get_latest_observation()
    show_observation(obs)

    forecast_data = api.get_forecast(days=6)  # next 2 days
    show_forecast(forecast_data)

if __name__ == "__main__":
    main()