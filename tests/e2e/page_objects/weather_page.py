from pageo.base_page import BasePage
from pageo.locators import IdLocator


from tests.e2e.common.URLs import URLs


class WeatherPage(BasePage):
    """
    Класс представляет собой страницу, где можно получить
    информацию о погодо по введенному городу в поле ввода.
    """
    base_url = URLs.BASE_URL
    url_suffix = URLs.WEATHER_SUFFIX

    city_field = IdLocator("cityInput")
    send_city_button = IdLocator("sendCity")
    