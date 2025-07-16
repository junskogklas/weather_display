# Coordinates for middle of Stockholm
DEFAULT_COORDS = {
    "lon": 18.0374,
    "lat": 59.3432
}

# Base entry point for the SMHI meteorological observations API
API_ENTRYPOINT = "https://opendata-download-metobs.smhi.se/api.json"
API_BASE = "https://opendata-download-metobs.smhi.se/api"

# Forecast API endpoint template (Lat & Lon decimal degrees)
FORECAST_URL = (
    "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/"
    "version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"
)

# Optional: define parameters you care about (e.g., temperature, wind speed, etc.)
# These names match SMHI internal parameter IDs
OBSERVED_PARAMETERS = {
    "temperature": 1,    # Air temperature
    "wind_speed": 4,     # Wind speed
    "humidity": 6,       # Relative humidity
    "air_pressure": 9,   # Air pressure
    "precipitation": 5,  # Precipitation amount
}

# Default station ID
DEFAULT_STATION_ID = 98230

# Default parameter ID to retrieve (for testing)
DEFAULT_PARAMETER_ID = OBSERVED_PARAMETERS["temperature"]

DEFAULT_PERIOD = "latest-hour"

# Construct final data URL template
# Format: https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/{param}/station/{station}/period/{period}/data.json
DATA_URL_TEMPLATE = (
    "https://opendata-download-metobs.smhi.se/api/version/1.0/"
    "parameter/{param}/station/{station}/period/{period}/data.json"
)
