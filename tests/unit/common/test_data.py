# Все описания взяты с https://openweathermap.org/weather-conditions
from datetime import time

WEATHER_DESCRIPTION = (
    "thunderstorm with light rain",
    "thunderstorm with rain",
    "thunderstorm with heavy rain",
    "light thunderstorm",
    "thunderstorm",
    "heavy thunderstorm",
    "ragged thunderstorm",
    "thunderstorm with light drizzle",
    "thunderstorm with drizzle",
    "thunderstorm with heavy drizzle",
    "light intensity drizzle",
    "drizzle",
    "heavy intensity drizzle",
    "light intensity drizzle rain",
    "drizzle rain",
    "heavy intensity drizzle rain",
    "shower rain and drizzle",
    "heavy shower rain and drizzle",
    "shower drizzle",
    "light rain",
    "moderate rain",
    "heavy intensity rain",
    "very heavy rain",
    "extreme rain",
    "freezing rain",
    "light intensity shower rain",
    "shower rain",
    "heavy intensity shower rain",
    "ragged shower rain",
    "light snow",
    "snow",
    "heavy snow",
    "sleet",
    "light shower sleet",
    "shower sleet",
    "light rain and snow",
    "rain and snow",
    "light shower snow",
    "shower snow",
    "heavy shower snow",
    "mist",
    "smoke",
    "haze",
    "sand/dust whirls",
    "fog",
    "sand",
    "dust",
    "volcanic ash",
    "squalls",
    "tornado",
    "clear sky"
)

NIGHT_TIME_BOUNDARY = [
    time(hour=7, minute=59),
]

DAY_TIME_BOUNDARU = [
    time(hour=18, minute=59),
]

NIGHT_TIME = [time(hour=h) for h in (0, 1, 2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 23)] + NIGHT_TIME_BOUNDARY
DAY_TIME = [time(hour=h) for h in range(8, 19)] + DAY_TIME_BOUNDARU

WROND_WEATHER_DESCRIPTION = (
    "",
    "aboba",
    "clearsky",
    "clear_sky",
    "dast",
    "smk",
    "oifh928h8f9289",
    "*!&#*&wjkedjwen",
)