from datetime import timedelta, datetime, date, time
from typing import TypeAlias

from weather_app.weather.constants import WEATHER_ICON_DAY, WEATHER_ICON_HIGHT

SecondsShift: TypeAlias = int


def add_seconds_shift_to_datetime(date_time: datetime, shift: SecondsShift) -> tuple[date, time]:
    """
    Добавляет к переданному времени сдвиг относительно UTC.
    """
    shift_in_hours = timedelta(seconds=shift)
    datetime_with_shift = date_time + shift_in_hours
    return datetime_with_shift.date(), datetime_with_shift.time()


def get_weater_icon_by_description(descrption: str, time_: time) -> str:
    """
    Возвращает иконку погоду по переданному описанию.

    Если время ночное, то возвращается темная иконка.
    """
    try:
        if is_hight(time_):
            return WEATHER_ICON_HIGHT[descrption]
        return WEATHER_ICON_DAY[descrption]
    except KeyError:
        return "no_image.png"
    

def is_hight(time_: time) -> bool:
    hours = time_.hour
    return 0 <= hours <= 7 or 19 <= hours <= 23


if __name__ == "__main__":
    a = time(hour=2)
    print(get_weater_icon_by_description("qwe", a))