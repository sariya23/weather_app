from selenium.webdriver.remote.webdriver import WebDriver
import pytest
import imagehash
from PIL import Image

from pathlib import Path
import io

from tests.e2e.common.window_sizes import ALL_WINDOW_SIZES
from tests.e2e.page_objects.weather_page import WeatherPage
from tests.e2e.common.image_by_link import ImageByLink


@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_base_image_present(driver: WebDriver, window_size: tuple[int, int]) -> None:
    """
    Проверяем, что на странице, когда еще не ввели город, отображается картинка.

    Как проверяем:
    1. Получаем картинку из приложения;
    2. Смотрим, что это ожидаемая картинка.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    image_element = weather_page.gopher_wait_image
    image_src = image_element.get_attribute("src")
    image = ImageByLink(image_src)
    expected_image_hash = imagehash.average_hash(Image.open(Path("../../src/static/images/gopher_info/gopher_play.png")))
    image_hash = imagehash.average_hash(Image.open(io.BytesIO(image.content)))
    assert expected_image_hash == image_hash