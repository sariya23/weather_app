import pytest

from datetime import time

from src.weather.utils import is_hight
from tests.unit.common.test_data import NIGHT_TIME


@pytest.mark.parametrize("time_", NIGHT_TIME)
def test_is_night(time_: time) -> None:
    """
    Проверяем, что ночь по времени определяется верно.
    """
    result_is_night = is_hight(time_)
    assert result_is_night is True

# @pytest.mark.parametrize("weather_description", WEATHER_DESCRIPTION)
# def test_get_weater_icon_by_description_day_positive(weather_description: str) -> None:
#     """
#     Проверяем, что при передаче функции верного описания погоды нам
#     возвращается нужное изображение этой погоды. 

#     Здесь проверяется при дневном времени.
#     """
#     weather_icon = get_weater_icon_by_description(weather_description, )
