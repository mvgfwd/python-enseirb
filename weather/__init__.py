#!/usr/bin/env python3
import requests
import json
import sys
import os.path
import platformdirs

CACHE_DIR = platformdirs.user_cache_dir('weather')


def weather_forecast(c):

    def cache_json(json_data):
        os.path.join(platformdirs.user_cache_dir('weather'))
        os.makedirs(CACHE_DIR, exist_ok=True)
        f = open(f'{CACHE_DIR}/{c.lower()}.json', 'w')
        f.write(json.dumps(json_data[0]))
        f.close()
    
    def retrieve_cache(city):
        f = open(f'{CACHE_DIR}/{city.lower()}.json', 'r')
        data = json.load(f)
        LON = data['lon']
        LAT = data['lat']
        return LON, LAT
    
    def req_coord():
        URL_COORDCITY_API = f'https://nominatim.openstreetmap.org/search?q={c}&format=json'
        city_coord_api = requests.get(URL_COORDCITY_API, headers={"User-Agent": "Mozilla/5.0"})
        wd_sc = city_coord_api.content
        if city_coord_api.status_code == 200 and len(wd_sc) > 2 :
            json_data = json.loads(wd_sc)
            LONG = json_data[0]['lon']
            LAT = json_data[0]['lat']
            get_weather(LONG, LAT)
            cache_json(json_data)
        else:
            raise ValueError("Location Not Found")
        
    try:
        with open(f'{CACHE_DIR}/{c.lower()}.json', 'r') as f:
            lonlat = retrieve_cache(c)
            get_weather(lonlat[0], lonlat[1])
            print(f'cache loaded {lonlat}')
    except FileNotFoundError:
        req_coord()
        print("fetching new data")
    except Exception as e:
        print(f'unexpected error => {e}')
        raise


def get_weather(long, lat):
    URL_FORECAST = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true'
    weather_api = requests.get(URL_FORECAST)
    weather_sc = weather_api.content
    json_data = json.loads(weather_sc)
    curr_temp = json_data['current_weather']['temperature']
    weather_code = json_data['current_weather']['weathercode']
    print_weather(curr_temp, weather_code)


def print_weather(temp, weather_code):
    if weather_codes.get(weather_code):
        print(f"{sys.argv[1]} has temp: {temp} °Celcius and {weather_codes[weather_code]}")
    else:
        print(f"{sys.argv[1]} has temp: {temp} °Celcius")
  
    
weather_codes = {
    0: "clear 👌🏻",
    1: "mostly clear 👌🏻",
    2: "partly cloudy",
    3: "cloudy",
    45: "fog",
    48: "freezing fog 🥶",
    51: "light drizzle 👌🏻",
    53: "drizzle 🥶",
    55: "heavy drizzle 🥶",
    56: "light freezing drizzle",
    57: "freezing drizzle",
    61: "light rain 👌🏻",
    63: "rain",
    65: "heavy rain 🥶",
    66: "light freezing rain",
    67: "freezing rain 🥶",
    71: "light snow",
    73: "snow",
    75: "heavy snow 🥶",
    77: "snow grains",
    80: "light rain shower 🌧️",
    81: "rain shower 🌧️",
    82: "heavy rain shower",
    85: "snow shower",
    86: "heavy snow shower",
    95: "thunderstorm 🌧️🌧️",
    96: "hailstorm",
    99: "heavy hailstorm 🥶"
}


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        weather_forecast(sys.argv[1])
    else:
        print("Please provide a city")
