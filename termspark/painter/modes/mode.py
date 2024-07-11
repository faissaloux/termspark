from abc import ABC, abstractmethod
from typing import Union


class Mode(ABC):
    @abstractmethod
    def format(self) -> Union[str, bool]:
        pass
