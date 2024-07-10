import re
from typing import Sequence, Union


class HEX:
    @staticmethod
    def check(color: Union[str, Sequence[str], None]) -> bool:
        if color is None:
            return False

        assert type(color) == str
        regex = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
        match = re.match(regex, color)

        return match is not None

    @staticmethod
    def to_rgb(color: str) -> tuple:
        color = color.lstrip("#")

        if len(color) == 3:
            color = "".join(2 * char for char in color)

        return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))
