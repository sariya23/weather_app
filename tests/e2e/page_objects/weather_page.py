from pageo.base_page import BasePage
from pageo.locators import IdLocator, ClassNameLocator, XPATHLocator

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
    buttons_with_city_names = XPATHLocator('//*/div[@class="buttons"]/button', is_many=True)
    city_name_span = IdLocator('city')
    datetime_span = IdLocator('datetime')
    weather_icon = IdLocator('weather_icon')
    temperature = IdLocator('temperature')
    wind_image = IdLocator('wind_image')
    wind_speed = IdLocator('wind_speed')
 