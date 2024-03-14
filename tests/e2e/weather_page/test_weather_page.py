from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import pytest

from pathlib import Path
from datetime import datetime, timedelta

from tests.e2e.common.image_by_link import ImageByLink
from tests.e2e.common.window_sizes import ALL_WINDOW_SIZES
from tests.e2e.page_objects.weather_page import WeatherPage
from tests.e2e.weather_page.utils import is_two_image_equal, get_button_by_text
from tests.e2e.weather_page.common.enable_input_test_data import INPUT_CITY_DATA
from tests.e2e.weather_page.common.city_names_test_data import (
    WRONG_CITY_NAMES,
    CITY_NAME_EXPECTED_EVAILABLE_CITIES,
)
from tests.e2e.weather_page.common.text_values import TextValues
from tests.e2e.weather_page.common.weather_info_test_data import CITY_BUTTON_TO_CLICK_EXPECTED_CITY_NAME


@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_base_image_text_present(
    driver: WebDriver, window_size: tuple[int, int]
) -> None:
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
    assert is_two_image_equal(
        image_from_page.content,
        Path("../../src/static/images/gopher_info/gopher_play.png"),
    )
    assert weather_page.no_city_city.text == TextValues.TEXT_WITH_NO_CITY_ENTER


@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_send_city_button_disabled(
    driver: WebDriver, window_size: tuple[int, int]
) -> None:
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
def test_send_city_button_enabled(
    driver: WebDriver, window_size: tuple[int, int], input_data: str
) -> None:
    """
    Проверяем, что при непустом поле ввода, кнопка активна.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    weather_page.city_field.send_keys(input_data)
    assert weather_page.send_city_button.is_enabled() is True


@pytest.mark.parametrize("city_name", WRONG_CITY_NAMES)
@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_image_text_when_wrong_city_name(
    driver: WebDriver, window_size: tuple[int, int], city_name: str
) -> None:
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
    assert is_two_image_equal(
        image_from_page.content,
        Path("../../src/static/images/gopher_info/gopher_fix.png"),
    )
    assert weather_page.no_city_city.text == TextValues.TEXT_WRONG_CITY


@pytest.mark.parametrize(
    "city_name, expected_city_list", CITY_NAME_EXPECTED_EVAILABLE_CITIES
)
@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_list_of_available_cities(
    driver: WebDriver,
    city_name: str,
    window_size: tuple[int, int],
    expected_city_list: list[str],
) -> None:
    """
    Проверяем, что после ввода города и нажатия кнопки
    появляется несколько кнопок с названиями похожих городов.

    Как проверяем:
    1. Вводим название города в поле;
    2. Нажимаем на кнопку "Посмотреть список доступных городов";
    3. Сравниваем полученный список городов с ожидаемым.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    weather_page.city_field.send_keys(city_name)
    weather_page.send_city_button.click()
    city_buttons = weather_page.buttons_with_city_names
    city_names_from_buttons = [city_button.text for city_button in city_buttons]
    assert sorted(city_names_from_buttons) == sorted(expected_city_list)


@pytest.mark.parametrize("city_input, button_text_to_click, expected_city_name_in_info, UTC_shift", CITY_BUTTON_TO_CLICK_EXPECTED_CITY_NAME)
@pytest.mark.parametrize("window_size", ALL_WINDOW_SIZES)
def test_weather_info(
    driver: WebDriver,
    city_input: str,
    expected_city_name_in_info: str,
    window_size: tuple[int, int],
    button_text_to_click: str,
    UTC_shift: int
) -> None:
    """
    Проверяем, что в информации о погоде отображаются верные данные, такие как:
    - Есть название города, время и дата;
    - Есть иконка погоды;
    - Есть иконка ветра;
    - Есть температура;
    - Есть сдвиг по UTC;
    - Есть скорость ветра.
    """
    weather_page = WeatherPage(driver, window_size=window_size)
    weather_page.city_field.send_keys(city_input)
    weather_page.send_city_button.click()

    button_to_click = get_button_by_text(weather_page.buttons_with_city_names, button_text_to_click)
    button_to_click.click()  # type: ignore

    city_in_info = weather_page.city_name_span.text
    assert city_in_info == expected_city_name_in_info

    date_in_info, time_in_info, utc_shift_in_info = weather_page.datetime_span.text.split(', ')
    local_datetime = datetime.utcnow() + timedelta(hours=UTC_shift)
    local_date = local_datetime.date().strftime("%d.%m.%Y")
    local_time = local_datetime.time().strftime("%H:%M")
    utc_shift_in_info = int(weather_page.UTC_shift.text.split()[1])
    assert utc_shift_in_info == UTC_shift
    assert local_date == date_in_info
    assert local_time == time_in_info

    weather_icon_src = weather_page.weather_icon.get_attribute("src")
    weather_image = ImageByLink(weather_icon_src)
    wind_icon_src = weather_page.wind_image.get_attribute("src")
    wind_speed_image = ImageByLink(wind_icon_src)
    assert wind_speed_image.is_image()
    assert weather_image.is_image() is True

    temperature_value, unit_temperature = weather_page.temperature.text.split()
    temperature_value = temperature_value.replace('.', '')
    assert temperature_value.isdigit() and unit_temperature == TextValues.CELSIUS

    wind_speed_value, unit_speed = weather_page.wind_speed.text.split()
    wind_speed_value = wind_speed_value.replace('.', '')
    assert wind_speed_value.isdigit() and unit_speed == TextValues.SPEED_UNIT