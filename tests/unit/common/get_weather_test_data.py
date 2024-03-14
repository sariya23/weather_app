from src.weather.service import Coordinates, Weather


COORDINATES_EXPECTED_CITY_POSITIVE = (
    [Coordinates(lat="55.7522", lon="37.6156"), Weather(city="Moscow", country="RU", temperature=0, wind_speed="", description="", UTC_shift=3600*3)],
    [Coordinates(lat="-15.7797", lon="-47.9297"), Weather(city="Brasília", country="BR", temperature=0, wind_speed="", description="", UTC_shift=-3*3600)],
)