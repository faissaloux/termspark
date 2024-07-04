from termspark.exceptions.printer_arg_error import PrinterArgError
from termspark.painter.constants.highlight import Highlight


class TestPrinterArgError:
    def test_exception_attributes(self):
        exception = PrinterArgError("left")
        assert exception.position == "left"

    def test_exception_dynamic_message(self):
        left_exception = PrinterArgError("left")
        assert all(
            word in str(left_exception)
            for word in [
                "print_left()",
                str(Highlight.RED).replace(",", ";"),
                " doesn't accept lists, maybe you wanna use ",
                "255;0;0",  # Red.
                " spark_left()",
                "0;0;255",  # Blue.
            ]
        )

        center_exception = PrinterArgError("center")
        assert all(
            word in str(center_exception)
            for word in [
                "print_center",
                str(Highlight.RED).replace(",", ";"),
                " doesn't accept lists, maybe you wanna use ",
                "255;0;0",  # Red.
                " spark_center",
                "0;0;255",  # Blue.
            ]
        )

        right_exception = PrinterArgError("right")
        assert all(
            word in str(right_exception)
            for word in [
                "print_right",
                str(Highlight.RED).replace(",", ";"),
                " doesn't accept lists, maybe you wanna use ",
                "255;0;0",  # Red.
                " spark_right",
                "0;0;255",  # Blue.
            ]
        )
