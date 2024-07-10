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
