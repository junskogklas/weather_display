# src/weather_display/main.py

from weather_api import WeatherAPI
from display import show_observation

def main():
    api = WeatherAPI()
    observation = api.get_latest_observation()
    show_observation(observation)

if __name__ == "__main__":
    main()
