
from weather_api import WeatherAPI
from display import WeatherDisplay
from datetime import datetime
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true",
                        help="Run in live mode (fullscreen, auto-refresh)")
    parser.add_argument("--freq", type=int, default=15,
                        help="Refresh frequency in minutes (only in live mode)")
    args = parser.parse_args()

    api = WeatherAPI()

    def update():
        observation = api.get_latest_observation()
        forecast = api.get_forecast(days=4)
        for day in forecast:
            dt = datetime.strptime(day["date"], "%Y-%m-%d")
            day["weekday"] = dt.strftime("%a").upper()
        return observation, forecast

    observation, forecast = update()
    display = WeatherDisplay(observation, forecast, fullscreen=args.live,
                             refresh_freq=args.freq if args.live else None)

    if args.live:
        refresh_interval_ms = args.freq * 60 * 1000

        def refresh():
            obs, fc = update()
            display.root.destroy()
            new_display = WeatherDisplay(obs, fc, fullscreen=True,
                                         refresh_freq=args.freq)
            new_display.root.after(refresh_interval_ms, refresh)
            new_display.run()

        display.root.after(refresh_interval_ms, refresh)

    display.run()

if __name__ == "__main__":
    main()

