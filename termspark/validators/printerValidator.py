from ..exceptions.printerArgException import PrinterArgException


class PrinterValidator:
    def validate(self, content, color, highlight):
        if any(
            [
                isinstance(content, list),
                isinstance(color, list),
                isinstance(highlight, list),
            ]
        ):
            raise PrinterArgException("left")
