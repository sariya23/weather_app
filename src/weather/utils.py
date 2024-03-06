from datetime import timedelta, datetime, date, time
from typing import TypeAlias

from src.weather.exceptions import WrongWeatherDescriprion


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
    weather_icon_map_day = {
        "clear_sky": "01d.png",
        "few_clouds": "02d.png",
        "scattered clouds": "03d.png",
        "broken clouds": "04d.png",
        "shower rain": "09d.png",
        "rain": "10d.png",
        "thunderstorm": "11d.png",
        "snow": "13d.png",
        "mist": "50d.ong"
    }

    weather_icon_map_night = {
        "clear_sky": "01n.png",
        "few_clouds": "02n.png",
        "scattered clouds": "03n.png",
        "broken clouds": "04n.png",
        "shower rain": "09n.png",
        "rain": "10n.png",
        "thunderstorm": "11n.png",
        "snow": "13n.png",
        "mist": "50n.ong"
    }
    try:
        if is_hight(time_):
            return weather_icon_map_night[descrption]
        return weather_icon_map_day[descrption]
    except KeyError:
        raise WrongWeatherDescriprion(f"Такой погоды нет - {descrption}")
    

def is_hight(time_: time) -> bool:
    hours = time_.hour
    return 0 < hours < 7 and 20 < hours < 23


if __name__ == "__main__":
    a = time(hour=2)
    print(get_weater_icon_by_description("qwe", a))