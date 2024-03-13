import pytest

from tests.unit.common.get_city_locations_with_same_name_test_data import POSITIVE_CITY_EXPECTED_LOCATION
from src.weather.service import get_city_locations_with_same_name, CityLocation


@pytest.mark.parametrize("city_name, expected_locations", POSITIVE_CITY_EXPECTED_LOCATION)
def test_get_city_locations_with_same_names(city_name: str, expected_locations: set[CityLocation]) -> None:
    """
    Проверяем, функция переводит название города на русский, если это возможно. И если 
    есть несколько городов с одинаковым названием, то она их все вернет.
    """ 
    cities = get_city_locations_with_same_name(city_name)
    assert cities == expected_locations

