from src.weather.service import Weather


POSITIVE_CITY_EXPECTED_WEATHER = (
    ["Moscow", Weather(location="Moscow", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["moscow", Weather(location="moscow", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Москва", Weather(location="Москва", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["москва", Weather(location="москва", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["москвА", Weather(location="москвА", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Санкт-Петербург", Weather(location="Санкт-Петербург", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Saint Petersburg", Weather(location="Saint Petersburg", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["saint petersburg", Weather(location="saint petersburg", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Гусь-Хрустальный", Weather(location="Гусь-Хрустальный", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Gus-Khrustalny", Weather(location="Gus-Khrustalny", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Gus-KhrustalnY",  Weather(location="Gus-KhrustalnY", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Казань",  Weather(location="Казань", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Kazan",  Weather(location="Kazan", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Ям", Weather(location="Ям", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Yam", Weather(location="Yam", temperature=0, wind_speed="", description="", UTC_shift=3*3600)],
    ["Лондон", Weather(location="Лондон", temperature=0, wind_speed="", description="", UTC_shift=0)],
    ["Пхукет", Weather(location="Пхукет", temperature=0, wind_speed="", description="", UTC_shift=7*3600)],
    ["Вашингтон", Weather(location="Вашингтон", temperature=0, wind_speed="", description="", UTC_shift=-4*3600)],
)