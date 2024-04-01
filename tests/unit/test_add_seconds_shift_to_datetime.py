import pytest

from datetime import datetime, date, time

from weather_app.weather.utils import add_seconds_shift_to_datetime
from tests.unit.common.add_seconds_shift_to_datetime_test_data import POSTITVE_DATETIME_SHIFT


@pytest.mark.parametrize("datetime_, shift, expected_date, expected_time", POSTITVE_DATETIME_SHIFT)
def test_add_seconds_to_datetime(datetime_: datetime, shift: int, expected_date: date, expected_time: time) -> None:
    """
    Проверяем, что дата и время увеличиваются на переданное кол-во
    секунд.
    """
    new_date, new_time = add_seconds_shift_to_datetime(datetime_, shift)
    assert new_date == expected_date and new_time == expected_time

