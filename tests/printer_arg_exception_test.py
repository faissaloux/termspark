from termspark.exceptions.printerArgException import PrinterArgException
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestPrinterArgException:
    def test_exception_attributes(self):
        exception = PrinterArgException('left')
        assert exception.position == 'left'

    def test_exception_dynamic_message(self):
        left_exception = PrinterArgException('left')
        assert all(word in str(left_exception) for word in ['print_left', str(Highlight.RED), ' doesn\'t accept lists, maybe you wanna use ', str(Fore.RED), ' spark_left', str(Highlight.BLUE)])

        center_exception = PrinterArgException('center')
        assert all(word in str(center_exception) for word in ['print_center', str(Highlight.RED), ' doesn\'t accept lists, maybe you wanna use ', str(Fore.RED), ' spark_center', str(Highlight.BLUE)])

        right_exception = PrinterArgException('right')
        assert all(word in str(right_exception) for word in ['print_right', str(Highlight.RED), ' doesn\'t accept lists, maybe you wanna use ', str(Fore.RED), ' spark_right', str(Highlight.BLUE)])