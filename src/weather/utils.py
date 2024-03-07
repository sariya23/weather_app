from datetime import timedelta, datetime, date, time
from typing import TypeAlias

from src.weather.exceptions import WrongWeatherDescriprion
from src.weather.constants import WEATHER_ICON_DAY, WEATHER_ICON_HIGHT

SecondsShift: TypeAlias = int


def get_datetime_by_utc_shift(date_time: datetime, shift: SecondsShift) -> tuple[date, time]:
    """
    Добавляет к переданному времени сдвиг относительно UTC.
    """
    shift_in_hours = timedelta(hours=shift / 3600)
    now_datetime_utc = date_time + shift_in_hours
    return now_datetime_utc.date(), now_datetime_utc.time()


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
        raise WrongWeatherDescriprion(f"Такой погоды нет - {descrption}")
    

def is_hight(time_: time) -> bool:
    hours = time_.hour
    return 0 < hours < 7 and 20 < hours < 23


if __name__ == "__main__":
    a = time(hour=2)
    print(get_weater_icon_by_description("qwe", a))