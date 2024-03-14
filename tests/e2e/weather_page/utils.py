from PIL.Image import Image as ImageType
from PIL import Image
import imagehash
from selenium.webdriver.remote.webelement import WebElement

import io
from pathlib import Path
from typing import Iterable

from tests.e2e.common.exceptions import NoMatchesButtons


def is_two_image_equal(image1: bytes | ImageType | Path, image2: bytes | ImageType | Path) -> bool:
    """
    Возвращает True, если средние хэши изображений равный, иначе False.
    """
    if isinstance(image1, bytes):
        image1 = Image.open(io.BytesIO(image1))
    elif isinstance(image1, Path):
        image1 = Image.open(image1)
    
    if isinstance(image2, bytes):
        image2 = Image.open(io.BytesIO(image2))
    elif isinstance(image2, Path):
        image2 = Image.open(image2)
    
    return imagehash.average_hash(image1) == imagehash.average_hash(image2)


def get_button_by_text(buttons: Iterable[WebElement], button_text: str) -> WebElement:
    """
    Из списка кнопок возврщает ту, текст которой совпадает
    с переданным.
    """
    for button in buttons:
        if button.text == button_text:
            return button
    raise NoMatchesButtons

