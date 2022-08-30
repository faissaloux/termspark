from termspark import TermSpark
import pytest
from termspark.exceptions.printerArgException import PrinterArgException
from termspark.exceptions.printerSparkerMixException import PrinterSparkerMixException

class TestPrintersTest:
    def test_can_set_left_content(self):
        termspark = TermSpark()

        termspark.print_left('LEFT')
        assert termspark.left['content'] == 'LEFT'

    def test_can_set_left_color(self):
        termspark = TermSpark()

        termspark.print_left('LEFT', 'white')
        assert termspark.left['content'] == 'LEFT'
        assert termspark.left['color'] == 'white'

    def test_can_set_left_highlight(self):
        termspark = TermSpark()

        termspark.print_left('LEFT', 'white', 'red')
        assert termspark.left['content'] == 'LEFT'
        assert termspark.left['color'] == 'white'
        assert termspark.left['highlight'] == 'red'

    def test_can_set_right_content(self):
        termspark = TermSpark()

        termspark.print_right('RIGHT')
        assert termspark.right['content'] == 'RIGHT'

    def test_can_set_right_color(self):
        termspark = TermSpark()

        termspark.print_right('RIGHT', 'white')
        assert termspark.right['content'] == 'RIGHT'
        assert termspark.right['color'] == 'white'

    def test_can_set_right_highlight(self):
        termspark = TermSpark()

        termspark.print_right('RIGHT', 'white', 'blue')
        assert termspark.right['content'] == 'RIGHT'
        assert termspark.right['color'] == 'white'
        assert termspark.right['highlight'] == 'blue'

    def test_can_set_center_content(self):
        termspark = TermSpark()

        termspark.print_center('CENTER')
        assert termspark.center['content'] == 'CENTER'

    def test_can_set_center_color(self):
        termspark = TermSpark()

        termspark.print_center('CENTER', 'white')
        assert termspark.center['content'] == 'CENTER'
        assert termspark.center['color'] == 'white'

    def test_can_set_center_highlight(self):
        termspark = TermSpark()

        termspark.print_center('CENTER', 'white', 'green')
        assert termspark.center['content'] == 'CENTER'
        assert termspark.center['color'] == 'white'
        assert termspark.center['highlight'] == 'green'

    def test_raise_exception_when_passing_list_to_print_left(self):
        termspark = TermSpark()

        with pytest.raises(PrinterArgException):
            termspark.print_left(['LEFT', 'red'])
        assert termspark.left == {} # Default

    def test_raise_exception_when_passing_list_to_print_right(self):
        termspark = TermSpark()

        with pytest.raises(PrinterArgException):
            termspark.print_right(['RIGHT', 'blue'])
        assert termspark.right == {} # Default

    def test_raise_exception_when_passing_list_to_print_center(self):
        termspark = TermSpark()

        with pytest.raises(PrinterArgException):
            termspark.print_center(['CENTER', 'blue'])
        assert termspark.center == {} # Default

    def test_raise_exception_when_mix_printer_with_same_position_sparker(self):
        termspark = TermSpark()

        with pytest.raises(PrinterSparkerMixException):
            termspark.print_left('LEFT', 'red').print_center('CENTER', 'blue').spark_center(['CENTER', 'gray', 'blue'])
        assert termspark.printed == ['left', 'center']

    def test_can_mix_printer_with_different_position_sparker(self):
        termspark = TermSpark()
        termspark.print_left('LEFT', 'blue').spark_right(['RIGHT', 'gray', 'blue'])

        assert termspark.printed == ['left']
        assert termspark.left['content'] == 'LEFT'
        assert termspark.left['color'] == 'blue'
        assert termspark.right['content'] == ['RIGHT']
        assert termspark.right['color'] == ['gray']
        assert termspark.right['highlight'] == ['blue']