import pytest

from termspark.exceptions.printer_arg_error import PrinterArgError
from termspark.validators.printer_validator import PrinterValidator


class TestPrinterValidator:
    def test_validate_content(self):
        with pytest.raises(PrinterArgError):
            PrinterValidator("left").validate(["termspark"], "black", "green", "bold")

    def test_validate_color(self):
        with pytest.raises(PrinterArgError):
            PrinterValidator("right").validate("termspark", ["black"], "green", "bold")

    def test_validate_highlight(self):
        with pytest.raises(PrinterArgError):
            PrinterValidator("center").validate("termspark", "black", ["green"], "bold")

    def test_validate_style(self):
        with pytest.raises(PrinterArgError):
            PrinterValidator("center").validate("termspark", "black", "green", ["bold"])

    def test_validate_all(self):
        with pytest.raises(PrinterArgError):
            PrinterValidator("right").validate(
                ["termspark"], ["black"], ["green"], ["bold"]
            )
