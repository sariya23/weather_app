from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest

from typing import Generator


@pytest.fixture(scope="session")
def chrome_options() -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return options


@pytest.fixture(scope="session")
def driver(chrome_options: webdriver.ChromeOptions) -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome(chrome_options)
    yield driver
    driver.quit()

