from typing import Final

from ..exceptions.printer_arg_error import PrinterArgError


class PrinterValidator:
    def __init__(self, position: str):
        self.position: Final[str] = position

    def validate(self, content, color, highlight, style):
        if any(
            [
                isinstance(content, list),
                isinstance(color, list),
                isinstance(highlight, list),
                isinstance(style, list),
            ]
        ):
            raise PrinterArgError(self.position)
