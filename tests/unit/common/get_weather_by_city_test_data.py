from src.weather.service import Weather


CITY_POSITIVE = (
    "Moscow",
    "moscow",
    "Москва",
    "москва",
    "москвА",
    "Сантк-Петербург",
    "Saint Petersburg",
    "saint petersburg",
    "Гусь-Хрустальный",
    "Gus-Khrustalny",
    "GUs-KhrutalnY",
    "Казань",
    "Kazan",
)

WEATHER_POSITIVE = (
    Weather(location="Moscow", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Moscow", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Москва", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Москва", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Москва", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Сантк-Петербург", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Saint Petersburg", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Saint Petersburg", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Гусь-Хрустальный", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Gus-Khrustalny", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="GUs-Khrutalny", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Казань", temperature=0, wind_speed="", description="", UTC_shift=10800),
    Weather(location="Kazan", temperature=0, wind_speed="", description="", UTC_shift=10800),
)