from pageo.base_page import BasePage
from pageo.locators import IdLocator, ClassNameLocator

from tests.e2e.common.URLs import URLs


class WeatherPage(BasePage):
    """
    Класс представляет собой страницу, где можно получить
    информацию о погодо по введенному городу в поле ввода.
    """
    base_url = URLs.BASE_URL
    url_suffix = URLs.WEATHER_SUFFIX

    gopher_image = ClassNameLocator("gopher_image__image")
    city_field = IdLocator("cityInput")
    send_city_button = IdLocator("sendCity")
    no_city_city = ClassNameLocator("no_weather__text")
    