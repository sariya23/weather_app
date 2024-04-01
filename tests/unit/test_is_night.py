import pytest

from datetime import time

from tests.unit.common.is_hight_test_date import (
    NIGHT_TIME,
    DAY_TIME,
)
from weather_app.weather.utils import is_hight


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("time_", NIGHT_TIME)
def test_is_night(time_: time) -> None:
    """
    Проверяем, что ночь по времени определяется верно.
    """
    result_is_night = is_hight(time_)
    assert result_is_night is True


@pytest.mark.fast
@pytest.mark.unit
@pytest.mark.parametrize("time_", DAY_TIME)
def test_is_day(time_: time) -> None:
    """
    Проверяем, что при передаче функции is_hight дневного времени 
    она возвращает False.
    """
    result_is_night = is_hight(time_)
    assert result_is_night is False