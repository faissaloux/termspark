from typing import Final, Type, Union

from ..helpers.rgb import RGB
from .constants.color import Color
from .constants.fore import Fore
from .constants.highlight import Highlight


class Painter:
    SUFFIX: Final[str] = "m"
    RESET: Final[str] = "\x1b[0m"

    def __paint(self, color: Union[str, tuple], kind: Type[Color]) -> str:
        if type(color) == tuple:
            color = RGB.to_str(color)

        assert type(color) == str
        if hasattr(kind, color.upper()):
            color = getattr(kind, color.upper())

        assert type(color) == str
        color = color.replace("_", "")
        if color and RGB.check(color):
            return f"{kind.PREFIX}{color.replace(',', ';')}{self.SUFFIX}"

        return ""

    def paint_color(self, color: Union[str, tuple]) -> str:
        return self.__paint(color, Fore)

    def paint_highlight(self, highlight: Union[str, tuple]) -> str:
        return self.__paint(highlight, Highlight)
