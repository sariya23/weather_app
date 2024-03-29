import requests  # type: ignore

import math
from dataclasses import dataclass, field

from src.weather.config import API_KEY, BASE_URL
from src.weather.exceptions import APIWaetherFailed, APIWeatherBadResponse, WrongCityName


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
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}&limit=5"
    response = requests.get(url)
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
    try:
        response = requests.get(f"{BASE_URL}lat={coordinates.lat}&lon={coordinates.lon}&appid={API_KEY}&lang={lang}&units={units}")
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