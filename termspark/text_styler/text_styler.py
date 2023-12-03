from typing import Sequence

from .constants.style import Style


class TextStyler:
    PREFIX: str = "\x1b["
    SUFFIX: str = "m"

    def style(self, styles: Sequence[str]) -> str:
        code: str = ""

        for style in styles:
            if style and hasattr(Style, style.upper()):
                code += f"{self.PREFIX}{getattr(Style, style.upper())}{self.SUFFIX}"
            code += ""

        return code
