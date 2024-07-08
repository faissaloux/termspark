from typing import Final, Type, Union

from ..helpers.rgb import RGB
from .constants.color import Color
from .constants.fore import Fore
from .constants.highlight import Highlight


class Painter:
    SUFFIX: Final[str] = "m"
    RESET: Final[str] = "\x1b[0m"

    def __paint(self, color: Union[str, tuple], kind: Type[Color]) -> str:
        color_str: str = color if type(color) == str else RGB.to_str(color)

        color_str = getattr(kind, color_str.upper(), color_str)

        color_str = color_str.replace("_", "")
        if color_str and RGB.check(color_str):
            return f"{kind.PREFIX}{color_str.replace(',', ';')}{self.SUFFIX}"

        return ""

    def paint_color(self, color: Union[str, tuple]) -> str:
        return self.__paint(color, Fore)

    def paint_highlight(self, highlight: Union[str, tuple]) -> str:
        return self.__paint(highlight, Highlight)
