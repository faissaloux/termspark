from ..exceptions.printerArgException import PrinterArgException


class PrinterValidator:
    def __init__(self, position: str):
        self.position = position

    def validate(self, content, color, highlight, style):
        if any(
            [
                isinstance(content, list),
                isinstance(color, list),
                isinstance(highlight, list),
                isinstance(style, list),
            ]
        ):
            raise PrinterArgException(self.position)
