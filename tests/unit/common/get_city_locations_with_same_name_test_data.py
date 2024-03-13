from src.weather.service import CityLocation, Coordinates


POSITIVE_CITY_EXPECTED_LOCATION = (
    ["Анапа", {CityLocation(Coordinates("0", "0"), city="Анапа", country="RU")}],
    [
        "Вашингтон",
        {
            CityLocation(Coordinates("0", "0"), city="Вашингтон", country="US"),
            CityLocation(Coordinates("0", "0"), city="Washington", country="NL"),
        },
    ],
    ["анАПА", {CityLocation(Coordinates("0", "0"), city="Анапа", country="RU")}],
    ["Anapa", {CityLocation(Coordinates("0", "0"), city="Анапа", country="RU")}],
)

NEGATIVE_CITY_EXPECTED_LOCATION = ("abobus", "8237489389e", "NEONAPA")
