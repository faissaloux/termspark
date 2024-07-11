import re
from typing import Union

from .mode import Mode
from .rgb import RGB


class HEX(Mode):
    def __init__(self, color: Union[str, tuple]):
        self.__color = color

    @staticmethod
    def check(color: Union[str, tuple, None]) -> bool:
        if type(color) != str:
            return False

        regex = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
        match = re.match(regex, color)

        return match is not None

    @staticmethod
    def to_rgb(color: str) -> tuple:
        color = color.lstrip("#")

        if len(color) == 3:
            color = "".join(2 * char for char in color)

        return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))

    def format(self) -> Union[str, bool]:
        assert type(self.__color) == str

        return RGB(self.to_rgb(self.__color)).format()
