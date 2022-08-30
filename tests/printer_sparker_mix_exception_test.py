from termspark.exceptions.printerSparkerMixException import PrinterSparkerMixException
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestPrinterSparkerMixException:
    def test_exception_attributes(self):
        exception = PrinterSparkerMixException('left')
        assert exception.position == 'left'

    def test_exception_dynamic_message(self):
        left_exception = PrinterSparkerMixException('left')
        assert all(word in str(left_exception) for word in [
            "can't use ",
            " print_left() ",
            str(Highlight.RED),
            ' with ',
            str(Fore.RED),
            ' spark_left()',
            str(Highlight.RED),
            ' you can replace ',
            str(Fore.BLUE),
            str(Highlight.BLUE),
        ])

        center_exception = PrinterSparkerMixException('center')
        assert all(word in str(center_exception) for word in [
            "can't use ",
            " print_center() ",
            str(Highlight.RED),
            ' with ',
            str(Fore.RED),
            ' spark_center()',
            str(Highlight.RED),
            ' you can replace ',
            str(Fore.BLUE),
            str(Highlight.BLUE),
        ])

        right_exception = PrinterSparkerMixException('right')
        assert all(word in str(right_exception) for word in [
            "can't use ",
            " print_right() ",
            str(Highlight.RED),
            ' with ',
            str(Fore.RED),
            ' spark_right()',
            str(Highlight.RED),
            ' you can replace ',
            str(Fore.BLUE),
            str(Highlight.BLUE),
        ])