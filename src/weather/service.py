import requests  # type: ignore

import math
from dataclasses import dataclass
from pprint import pprint

from src.weather.config import API_KEY, BASE_URL
from src.weather.exceptions import APIWaetherFailed, APIWeatherBadResponse


@dataclass(frozen=True, slots=True)
class Weather:
    location: str
    temperature: int
    wind_speed: str
    description: str
    UTC_shift: int

def get_weather_by_city(city: str, lang: str = "en", units: str = "metric") -> Weather:
    try:
        response = requests.get(f"{BASE_URL}q={city}&appid={API_KEY}&lang={lang}&units={units}")
        result_data = response.json()
        print(result_data)
        result = {
            "location": city,
            "temperature": math.ceil((result_data["main"]["temp"])),
            "wind_speed": result_data["wind"]["speed"],
            "description": result_data["weather"][0]["description"],
            "UTC_shift": result_data["timezone"]
        }
        return Weather(**result)

    except requests.exceptions.RequestException:
        raise APIWaetherFailed

    except KeyError:
        raise APIWeatherBadResponse
    except Exception as e:
        raise e


# print(get_weather_by_city("Вашингтон"))
# print(get_weather_by_city("Washington, D.C."))
# print(get_weather_by_city("Пхукет"))
# print(get_weather_by_city("Сантаё-Фе"))
# print(get_weather_by_city("Moscow"))


url = f"http://api.openweathermap.org/geo/1.0/direct?q=Вашингтон&&appid={API_KEY}&limit=5"
res = requests.get(url).json()
pprint(res)
lat, lon = res[0]["lat"], res[0]["lon"]
url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
res_weather = requests.get(url_weather)
print(res_weather.json()["timezone"])