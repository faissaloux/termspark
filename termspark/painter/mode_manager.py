from typing import Union

from termspark.painter.modes.hex import HEX
from termspark.painter.modes.name import Name
from termspark.painter.modes.rgb import RGB


class ModeManager:
    __mode: Union[RGB, HEX, Name]

    def __init__(self, color: Union[str, tuple]):
        self._color = color

        if RGB.check(color):
            self.__mode = RGB(color)
        elif HEX.check(color):
            self.__mode = HEX(color)
        else:
            self.__mode = Name(color)

    def format(self):
        return self.__mode.format()
