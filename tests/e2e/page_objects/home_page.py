from pageo.base_page import BasePage
from pageo.locators import IdLocator, XPATHLocator

from tests.e2e.common.URLs import URLs


class HomePage(BasePage):
    base_url = URLs.BASE_URL

    to_weather_page_link = IdLocator("weather_link")
    to_home_page_link = IdLocator("home_link")
    burger_menu = XPATHLocator('/html/body/nav/div/button')