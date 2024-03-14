import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from tests.e2e.page_objects.home_page import HomePage
from tests.e2e.page_objects.weather_page import WeatherPage
from tests.e2e.common.window_sizes import MOBILE_WINDOW_SIZES


@pytest.mark.parametrize("window_size", MOBILE_WINDOW_SIZES)
def test_burger(driver: WebDriver, window_size: tuple[int, int]) -> None:
    """
    Проверяем, что на мобильных экранах есть бургер меню и оно работает.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    home_page = HomePage(driver, window_size=window_size, is_open=False)

    weather_page.burger_menu.click()
    weather_page.to_home_page_link.click()
    assert driver.current_url == home_page.url

    home_page = HomePage(driver, window_size=window_size)
    home_page.burger_menu.click()
    driver.implicitly_wait(20)
    home_page.to_weather_page_link.click()
    assert driver.current_url == weather_page.url