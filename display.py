from PIL import Image

from config import Config, load_config
from lib import get_display_driver


class Display:
    def __init__(self):
        self.config: Config = load_config()
        self._epaper_driver = self.__init_driver()
        self._width, self._height = self.__display_size()

    def __init_driver(self):
        if self.config:
            return get_display_driver(display_type=self.config.display_type)
        return None

    def __display_size(self):
        if self._epaper_driver:
            return self._epaper_driver.width, self._epaper_driver.height

    def init_display(self):
        self._epaper_driver.init()

    def clear_display(self):
        self._epaper_driver.clear(0xFF)

    def partial_draw(self, image: Image):
        self._epaper_driver.displayPartial(image=image)

    def draw(self, image: Image):
        self._epaper_driver.displayPartBaseImage(image=image)

    def display(self, image: Image):
        self._epaper_driver.display(image=image)

    def to_bytes(self, image: Image):
        self._epaper_driver.getbuffer(image=image)

    @property
    def epaper_driver(self):
        return self._epaper_driver

    @property
    def size(self):
        return self.__display_size()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @classmethod
    def get_scaled_image(cls, image: Image):
        is_le = list(map(lambda x, y: x <= y, sorted(image.size), sorted(cls.size)))
        is_le = is_le[0] & is_le[1]
        if not is_le:
            resize_ratio = min([i / j for i, j in zip(cls.size, image.size)])
            image = image.resize(image.size * resize_ratio)
        return image
