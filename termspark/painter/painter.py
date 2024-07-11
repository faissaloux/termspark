from typing import Final, Type, Union

from .constants.color import Color
from .constants.fore import Fore
from .constants.highlight import Highlight
from .mode_manager import ModeManager


class Painter:
    SUFFIX: Final[str] = "m"
    RESET: Final[str] = "\x1b[0m"

    def __paint(self, color: Union[str, tuple], kind: Type[Color]) -> str:
        if color:
            color = ModeManager(color).format()

        if color:
            return f"{kind.PREFIX}{color}{self.SUFFIX}"

        return ""

    def paint_color(self, color: Union[str, tuple]) -> str:
        return self.__paint(color, Fore)

    def paint_highlight(self, highlight: Union[str, tuple]) -> str:
        return self.__paint(highlight, Highlight)
