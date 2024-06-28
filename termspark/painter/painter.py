import re
from typing import Final, Type

from .constants.color import Color
from .constants.fore import Fore
from .constants.highlight import Highlight


class Painter:
    SUFFIX: Final[str] = "m"
    RESET: Final[str] = "\x1b[0m"

    def __paint(self, color: str, type: Type[Color]) -> str:
        if color and self.__is_rgb(color):
            return f"{type.RGB_PREFIX}{color.replace(',', ';')}{self.SUFFIX}"

        if color and hasattr(type, color.upper()):
            return f"{type.PREFIX}{getattr(type, color.upper())}{self.SUFFIX}"

        return ""

    def paint_color(self, color: str) -> str:
        return self.__paint(color, Fore)

    def paint_highlight(self, highlight: str) -> str:
        return self.__paint(highlight, Highlight)

    def __is_rgb(self, color: str) -> bool:
        regex = r"(\d+),\s*(\d+),\s*(\d+)"
        match = re.match(regex, color)

        if match is None:
            return False

        return all(0 <= int(group) <= 255 for group in match.groups())
