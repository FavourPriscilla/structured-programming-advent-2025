"""
Simple Weather Forecast CLI

- If you have an OpenWeatherMap API key, set the environment variable OPENWEATHER_API_KEY
  or paste it when prompted. The script will fetch the real current weather.
- If you don't provide an API key, the script will generate a simple simulated forecast.

Requires (only for live API): requests
Install with: pip install requests
"""

import os
import random
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None  # we'll handle absence of requests if user chooses API mode

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_live_weather(city: str, api_key: str):
    if requests is None:
        raise RuntimeError("The 'requests' library is required for live API calls. Install it with: pip install requests")
    params = {"q": city, "appid": api_key, "units": "metric"}
    resp = requests.get(API_URL, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    # Extract useful fields
    weather = {
        "city": f"{data.get('name')}, {data.get('sys', {}).get('country')}",
        "description": data.get("weather", [{}])[0].get("description", "N/A").title(),
        "temp": data.get("main", {}).get("temp"),
        "feels_like": data.get("main", {}).get("feels_like"),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed")
    }
    return weather

def simulate_weather(city: str):
    conditions = ["Sunny", "Partly Cloudy", "Cloudy", "Light Rain", "Heavy Rain", "Thunderstorms", "Snow"]
    base = random.randint(15, 30)
    hi = base + random.randint(0, 6)
    lo = base - random.randint(2, 8)
    weather = {
        "city": city,
        "description": random.choice(conditions),
        "temp": round((hi + lo) / 2, 1),
        "feels_like": round((hi + lo) / 2 + random.uniform(-2, 2), 1),
        "humidity": random.randint(40, 90),
        "wind_speed": round(random.uniform(0.5, 8.0), 1)
    }
    return weather

def display(weather: dict):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\nWeather — {weather.get('city')}  ({now})")
    print("-" * 40)
    print(f"Condition : {weather.get('description')}")
    print(f"Temp      : {weather.get('temp')} °C")
    print(f"Feels like: {weather.get('feels_like')} °C")
    print(f"Humidity  : {weather.get('humidity')}%")
    print(f"Wind speed: {weather.get('wind_speed')} m/s")
    print("-" * 40)

def main():
    print("Simple Weather Forecast CLI")
    city = input("Enter city (e.g. London or 'London,GB'): ").strip()
    if not city:
        print("No city entered. Exiting.")
        return

    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if not api_key:
        # Offer to paste api key or skip
        candidate = input("Paste OpenWeatherMap API key (or press Enter to simulate forecast): ").strip()
        api_key = candidate or ""

    if api_key:
        try:
            weather = fetch_live_weather(city, api_key)
            display(weather)
        except Exception as e:
            print(f"Live API call failed: {e}")
            print("Falling back to a simulated forecast.\n")
            weather = simulate_weather(city)
            display(weather)
    else:
        weather = simulate_weather(city)
        display(weather)

if __name__ == "__main__":
    main()