from typing import Final


class Style:
    BOLD: Final[int] = 1
    DIM: Final[int] = 2
    ITALIC: Final[int] = 3
    UNDERLINE: Final[int] = 4
    CURLY_UNDERLINE: Final[str] = "4:3"
    DOTTED_UNDERLINE: Final[str] = "4:4"
    DASHED_UNDERLINE: Final[str] = "4:5"
    BLINK: Final[int] = 5
    REVERSE: Final[int] = 7
    HIDDEN: Final[int] = 8
    STRIKE_THROUGH: Final[int] = 9
    DOUBLE_UNDERLINE: Final[int] = 21
    OVERLINE: Final[int] = 53
