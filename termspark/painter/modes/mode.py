from abc import ABC, abstractmethod
from typing import Union


class Mode(ABC):
    @staticmethod
    @abstractmethod
    def check(color: Union[str, tuple, None]) -> bool:
        pass

    @abstractmethod
    def format(self) -> Union[str, bool]:
        pass
