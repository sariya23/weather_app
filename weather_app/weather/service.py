import requests  # type: ignore

import math
from dataclasses import dataclass, field

from weather_app.config import settings
from weather_app.weather.exceptions import APIWaetherFailed, APIWeatherBadResponse, WrongCityName


@dataclass(frozen=True, slots=True)
class Weather:
    city: str
    country: str
    temperature: int
    wind_speed: str
    description: str
    UTC_shift: int


@dataclass(frozen=True, slots=True)
class Coordinates:
    lat: str
    lon: str


@dataclass(frozen=True, slots=True)
class CityLocation:
    coordinates: Coordinates = field(compare=False)
    city: str
    country: str


def get_city_locations_with_same_name(city: str) -> set[CityLocation]:
    url = f"{settings.url_get_by_city_name}q={city}&appid={settings.weather_api}&limit=5"
    params = {
        "q": city,
        "appid": settings.weather_api,
        "limit": 5,
    }
    response = requests.get(url, params=params)
    result_data = response.json()
    
    if not result_data:
        raise WrongCityName

    cities: list[CityLocation] = []

    for city_data in result_data:
        coordinate = Coordinates(lat=city_data["lat"], lon=city_data["lon"])
        if city_data.get("local_names") and "ru" in city_data.get("local_names"):
            cities.append(
                CityLocation(
                    coordinates=coordinate,
                    city=city_data["local_names"]["ru"],
                    country=city_data["country"],
                )
            )
        else:
            cities.append(
                CityLocation(
                    coordinates=coordinate,
                    city=city_data["name"],
                    country=city_data["country"],
                )
            )

    return set(cities)


def get_weather_by_coordinates(coordinates: Coordinates, lang: str = "en", units: str = "metric") -> Weather:
    url = settings.url_get_by_coordinates
    params = {
        "lat": coordinates.lat,
        "lon": coordinates.lon,
        "appid": settings.weather_api,
        "lang": lang,
        "units": "metric",
    }
    try:
        response = requests.get(url, params=params)
        result_data = response.json()
        result = {
            "city": result_data["name"],
            "country": result_data["sys"]["country"],
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