from selenium.webdriver.remote.webdriver import WebDriver
import pytest

from tests.e2e.page_objects.weather_page import WeatherPage
from tests.e2e.page_objects.home_page import HomePage
from tests.e2e.common.window_sizes import DESKTOP_WINDOW_SIZES


@pytest.mark.parametrize("window_size", DESKTOP_WINDOW_SIZES)
def test_no_burger(driver: WebDriver, window_size: tuple[int, int]) -> None:
    """
    Проверяем, что на десктоп экранах нет меню бургера. Также проверяем, что
    при клике на ссылку в нав баре нас перекидывает на ожидаемый URL.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    home_page = HomePage(driver, is_open=False)
    assert weather_page.burger_menu.is_displayed() is False

    weather_page.to_home_page_link.click()
    assert driver.current_url == home_page.base_url