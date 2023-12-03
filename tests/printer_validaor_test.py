import pytest

from termspark.exceptions.printerArgException import PrinterArgException
from termspark.validators.printerValidator import PrinterValidator


class TestPrinterValidator:
    def test_validate_content(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator("left").validate(["termspark"], "black", "green", "bold")

    def test_validate_color(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator("right").validate("termspark", ["black"], "green", "bold")

    def test_validate_highlight(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator("center").validate("termspark", "black", ["green"], "bold")

    def test_validate_style(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator("center").validate("termspark", "black", "green", ["bold"])

    def test_validate_all(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator("right").validate(
                ["termspark"], ["black"], ["green"], ["bold"]
            )
