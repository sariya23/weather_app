from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import pytest

from pathlib import Path

from tests.e2e.common.window_sizes import ALL_WINDOW_SIZES
from tests.e2e.page_objects.weather_page import WeatherPage
from tests.e2e.common.image_by_link import ImageByLink
from tests.e2e.weather_page.utils import is_two_image_equal
from tests.e2e.weather_page.common.enable_input_test_data import INPUT_CITY_DATA
from tests.e2e.weather_page.common.wrong_city_names_test_data import WRONG_CITY_NAMES


@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_base_image_present(driver: WebDriver, window_size: tuple[int, int]) -> None:
    """
    Проверяем, что на странице, когда еще не ввели город, отображается картинка.

    Как проверяем:
    1. Получаем картинку из приложения;
    2. Смотрим, что это ожидаемая картинка.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    image_element = weather_page.gopher_image
    image_src = image_element.get_attribute("src")
    image_from_page = ImageByLink(image_src)
    assert is_two_image_equal(image_from_page.content, Path("../../src/static/images/gopher_info/gopher_play.png"))


@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_send_city_button_disabled(driver: WebDriver, window_size: tuple[int, int]) -> None:
    """
    Проверяем, что при определенных условиях, кнопка отправки города заблокировона.
    Кнопка заблокирована, когда поле ввода города путое.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    assert weather_page.send_city_button.is_enabled() is False

    weather_page.city_field.send_keys("aboba")
    weather_page.city_field.send_keys(Keys.CONTROL + "a")
    weather_page.city_field.send_keys(Keys.DELETE)

    assert weather_page.send_city_button.is_enabled() is False
    
    weather_page.city_field.send_keys(" " * 20)
    assert weather_page.send_city_button.is_enabled() is False


@pytest.mark.parametrize("input_data", INPUT_CITY_DATA)
@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_send_city_button_enabled(driver: WebDriver, window_size: tuple[int, int], input_data: str) -> None:
    """
    Проверяем, что при непустом поле ввода, кнопка активна.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    weather_page.city_field.send_keys(input_data)
    assert weather_page.send_city_button.is_enabled() is True


@pytest.mark.parametrize("city_name", WRONG_CITY_NAMES)
@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_image_when_wrong_city_name(driver: WebDriver, window_size: tuple[int, int], city_name: str) -> None:
    """
    Проверяем, что при вводе несуществующего города появляется изображение
    и поясняющий текст.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    weather_page.city_field.send_keys(city_name)
    weather_page.send_city_button.click()

    image_element = weather_page.gopher_image
    image_src = image_element.get_attribute("src")
    image_from_page = ImageByLink(image_src)
    assert is_two_image_equal(image_from_page.content, Path("../../src/static/images/gopher_info/gopher_fix.png"))
