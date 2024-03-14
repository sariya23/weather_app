from PIL.Image import Image as ImageType
from PIL import Image
import imagehash

import io
from pathlib import Path


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


