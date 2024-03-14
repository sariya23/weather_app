from functools import cached_property
import io

import urllib.request
import pyfsig
from PIL import Image


class ImageByLink:
    """
    Класс представляет изображение, которое скачивается по ссылке.
    """
    def __init__(self, link):
        self.link = link

    @cached_property
    def content(self) -> bytes:
        """
        Содержимое файла в байтовом представлении.
        """
        with urllib.request.urlopen(self.link) as file:
            return file.read()

    @cached_property
    def source_size(self) -> int:
        """
        Размер изображения в байтах
        """
        return len(self.content)

    @cached_property
    def size(self) -> tuple[int, int]:
        """
        Размер изображения в виде кортежа (X, Y) в пикселях.
        """
        image = Image.open(io.BytesIO(self.content))
        return image.size

    def get_file_extension(self) -> str:
        """
        Возвращает расширение файла.
        """
        file_signature = pyfsig.get_from_file(io.BytesIO(self.content))

        return file_signature[0]['file_extension']

    def is_image(self) -> bool:
        """
        Метод проверяет, что файл является изображением.
        """
        return self.get_file_extension() in ('jpg', 'png', 'jpeg')
