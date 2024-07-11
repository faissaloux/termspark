from importlib import import_module
from typing import Union

from .modes.mode import Mode


class ModeManager:
    def __init__(self, color: Union[str, tuple]):
        self._color = color

        for mode in Mode.__subclasses__():
            _module = import_module(f"termspark.painter.modes.{mode.__name__.lower()}")
            _class = getattr(_module, mode.__name__)
            if _class.check(color):
                self.__mode = _class(color)
                break

    def format(self):
        return self.__mode.format()
