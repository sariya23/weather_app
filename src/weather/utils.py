from datetime import timedelta, datetime, date, time
from typing import TypeAlias

SecondsShift: TypeAlias = int


def get_datetime_by_utc_shift(date_time: datetime, shift: SecondsShift) -> tuple[date, time]:
    """
    Добавляет к переданному времени сдвиг относительно UTC.
    """
    shift_in_hours = timedelta(hours=shift / 3600)
    now_datetime_utc = date_time + shift_in_hours
    return now_datetime_utc.date(), now_datetime_utc.time()
