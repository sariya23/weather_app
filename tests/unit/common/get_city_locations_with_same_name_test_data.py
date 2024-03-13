from src.weather.service import CityLocation

POSITIVE_CITY_EXPECTED_LOCATION = (
    ['Анапа', {CityLocation(lat=0.0, lon=0.0, city="Анапа", country="RU")}],
    ['Вашингтон', {CityLocation(lat=0.0, lon=0.0, city="Вашингтон", country="US"), CityLocation(lat=0.0, lon=0.0, city="Washington", country="NL")}]
)