import re
from typing import Sequence, Union

from .mode import Mode


class RGB(Mode):
    def __init__(self, color: Union[str, tuple]):
        self.__color = color if type(color) == str else RGB.to_str(color)

    @staticmethod
    def check(color: Union[str, Sequence[str], None]) -> bool:
        if color is None:
            return False

        if type(color) == tuple:
            if len(color) != 3:
                return False

            color = RGB.to_str(color)

        assert type(color) == str
        regex = r"(\d+),\s*(\d+),\s*(\d+)"
        match = re.match(regex, color)

        if match is None:
            return False

        return all(0 <= int(group) <= 255 for group in match.groups())

    @staticmethod
    def to_str(color: Union[str, tuple]) -> str:
        if type(color) == str:
            return color

        return ",".join([str(comp) for comp in color])

    def format(self) -> Union[str, bool]:
        self.__color = self.__color.replace("_", "")

        if self.check(self.__color):
            return self.__color.replace(",", ";")

        return False
