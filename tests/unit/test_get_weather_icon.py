import pytest

from datetime import time

from weather_app.weather.utils import get_weater_icon_by_description
from tests.unit.common.get_weather_icon_test_data import (
    NIGHT_TIME,
    DAY_TIME,
    WEATHER_DESCRIPTION,
    WROND_WEATHER_DESCRIPTION,
)
from weather_app.weather.constants import WEATHER_ICON_DAY, WEATHER_ICON_HIGHT
from weather_app.weather.exceptions import WrongWeatherDescriprion


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("time_", DAY_TIME)
@pytest.mark.parametrize("weather_description", WEATHER_DESCRIPTION)
def test_get_weater_icon_by_description_day_positive(weather_description: str, time_: time) -> None:
    """
    Проверяем, что при передаче функции верного описания погоды нам
    возвращается нужное изображение этой погоды. 

    Здесь проверяется при дневном времени.
    """
    weather_icon = get_weater_icon_by_description(weather_description, time_)
    assert weather_icon == WEATHER_ICON_DAY[weather_description]


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("time_", NIGHT_TIME)
@pytest.mark.parametrize("weather_description", WEATHER_DESCRIPTION)
def test_get_weater_icon_by_description_night_positive(weather_description: str, time_: time) -> None:
    """
    Проверяем, что при передаче функции верного описания погоды нам
    возвращается нужное изображение этой погоды. 

    Здесь проверяется при ночном времени.
    """
    weather_icon = get_weater_icon_by_description(weather_description, time_)
    assert weather_icon == WEATHER_ICON_HIGHT[weather_description]


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("wrong_weather_description", WROND_WEATHER_DESCRIPTION)
def test_get_weater_icon_by_description_negative(wrong_weather_description: str) -> None:
    """
    Проверяем, что при вводе описания погоды, которого нет в
    словаре, восбуждается исключение WrongWeatherDescriprion.
    """
    with pytest.raises(WrongWeatherDescriprion):
        get_weater_icon_by_description(wrong_weather_description, time())
