from typing import Union

from ..constants.color import Color
from .mode import Mode
from .rgb import RGB


class Name(Mode):
    def __init__(self, color: Union[str, tuple]):
        assert type(color) == str
        self.__color = getattr(Color, color.upper(), color)

    def format(self) -> Union[str, bool]:
        return RGB(self.__color).format()
