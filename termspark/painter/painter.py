from typing import Final

from .constants.fore import Fore
from .constants.highlight import Highlight


class Painter:
    PREFIX: Final[str] = "\x1b["
    SUFFIX: Final[str] = "m"
    RESET: Final[str] = "\x1b[0m"

    def __paint(self, color: str, type) -> str:
        if color and hasattr(type, color.upper()):
            return f"{self.PREFIX}{getattr(type, color.upper())}{self.SUFFIX}"
        return ""

    def paint_color(self, color: str) -> str:
        return self.__paint(color, Fore)

    def paint_highlight(self, highlight: str) -> str:
        return self.__paint(highlight, Highlight)
