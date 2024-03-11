import pytest

from src.weather.service import get_weather_by_city
from src.weather.service import Weather
from tests.unit.common.get_weather_by_city_test_data import POSITIVE_CITY_EXPECTED_WEATHER


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("city, expected_weather", POSITIVE_CITY_EXPECTED_WEATHER)
def test_get_weather_by_city_positive(city: str, expected_weather: Weather) -> None:
    weather: Weather = get_weather_by_city(city)
    print(weather)
    assert weather.location == expected_weather.location and weather.UTC_shift == expected_weather.UTC_shift
