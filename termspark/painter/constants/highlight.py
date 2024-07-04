from typing import Final

from termspark.painter.constants.color import Color


class Highlight(Color):
    PREFIX: Final[str] = "\x1b[48;2;"
