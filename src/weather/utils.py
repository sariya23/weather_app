from datetime import timedelta, datetime
from typing import TypeAlias

SecondsShift: TypeAlias = int


def get_datetime_by_utc_shift(date_time: datetime, shift: SecondsShift) -> datetime:
    """
    Добавляет к переданному времени сдвиг относительно UTC.
    """
    shift_in_hours = timedelta(hours=shift / 3600)
    return (date_time + shift_in_hours)
