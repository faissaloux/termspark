import pytest

from termspark.exceptions.printerArgException import PrinterArgException
from termspark.validators.printerValidator import PrinterValidator


class TestPrinterValidator:
    def test_validate_content(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator().validate(["termspark"], "black", "green")

    def test_validate_color(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator().validate("termspark", ["black"], "green")

    def test_validate_highlight(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator().validate("termspark", "black", ["green"])

    def test_validate_all(self):
        with pytest.raises(PrinterArgException):
            PrinterValidator().validate(["termspark"], ["black"], ["green"])
