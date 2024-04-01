import pytest

from tests.unit.common.get_city_locations_with_same_name_test_data import (
    POSITIVE_CITY_EXPECTED_LOCATION,
    NEGATIVE_CITY_EXPECTED_LOCATION,
)
from weather_app.weather.service import get_city_locations_with_same_name, CityLocation
from weather_app.weather.exceptions import WrongCityName

@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.parametrize("city_name, expected_locations", POSITIVE_CITY_EXPECTED_LOCATION)
def test_get_city_locations_with_same_name_positive(city_name: str, expected_locations: set[CityLocation]) -> None:
    """
    Проверяем, что функция переводит название города на русский, если это возможно. И если 
    есть несколько городов с одинаковым названием, то она их все вернет.
    """ 
    cities = get_city_locations_with_same_name(city_name)
    assert cities == expected_locations


@pytest.mark.unit
@pytest.mark.fast
@pytest.mark.parametrize("city_name", NEGATIVE_CITY_EXPECTED_LOCATION)
def test_get_city_locations_with_same_name_negative(city_name: str) -> None:
    """
    Проверяем, что при неверном вводе города возбуждается исключение. 
    """ 
    with pytest.raises(WrongCityName):
        get_city_locations_with_same_name(city_name)

