# Raspberry Pi Weather Display

A weather display written in Python for use with a Raspberry Pi and 7" display screen. It fetches and displays local weather observations (SMHI api) and a short-term forecast using a minimal black-and-white interface. 

SMHI API: https://opendata.smhi.se

Simple screen I chose for this project: https://www.amazon.com/dp/B0F3JFG4RS?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/junskogklas/weather_display.git
    cd weather_display
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running

**Development mode (default)**

```bash
python main.py
```

**Live mode (e.g. on Raspberry Pi, fullscreen + auto-refresh)**

```bash
python main.py --mode live --freq 15
```

- `--mode`: `debug` (default) or `live`
- `--freq` (optional): Refresh frequency in minutes (only applies to live mode)

## Configuration

- `q` exits fullscreen mode
- Refresh frequency and last updated time are shown in top right
- Screen resolution: 480x320
- Cursor is hidden in live mode

## Future Work

- Persist last update across restarts
- Settings for units and refresh time
- Scheduled sleep mode
- Features assuming interactive interface
