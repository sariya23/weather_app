import pytest

from weather_app.weather.service import get_weather_by_coordinates, Coordinates, Weather
from tests.unit.common.get_weather_test_data import COORDINATES_EXPECTED_CITY_POSITIVE


@pytest.mark.parametrize(
    "coordinates, expected_weather_object", COORDINATES_EXPECTED_CITY_POSITIVE
)
def test_get_weather_positive(
    coordinates: Coordinates, expected_weather_object: Weather
) -> None:
    """
    Проверяем, при передаче координат функция возвращает ожидаемые данные по этому месту.

    В тесте не проверяется погода и другие меняющиеся условия.
    """
    weather: Weather = get_weather_by_coordinates(coordinates)
    assert (
        weather.city == expected_weather_object.city
        and weather.UTC_shift == expected_weather_object.UTC_shift
        and weather.country == expected_weather_object.country
    )
