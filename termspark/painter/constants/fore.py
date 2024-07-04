from typing import Final

from termspark.painter.constants.color import Color


class Fore(Color):
    PREFIX: Final[str] = "\x1b[38;2;"
