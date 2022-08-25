from termspark import TermSpark
import pytest

class TestTermsparkAttributes:
    def test_can_set_separator(self):
        termspark = TermSpark()
        assert termspark.separator == ' ' # Default

        termspark.set_separator('.')
        assert termspark.separator == '.'

    def test_cant_set_more_than_one_char_separator(self):
        termspark = TermSpark()
        assert termspark.separator == ' ' # Default

        with pytest.raises(Exception):
            termspark.set_separator('..')
        assert termspark.separator == ' ' # Default

    def test_can_set_left_content(self):
        termspark = TermSpark()

        termspark.print_left('LEFT')
        assert termspark.left['content'] == 'LEFT'

    def test_can_set_right_content(self):
        termspark = TermSpark()

        termspark.print_right('RIGHT')
        assert termspark.right['content'] == 'RIGHT'

    def test_can_set_center_content(self):
        termspark = TermSpark()

        termspark.print_center('CENTER')
        assert termspark.center['content'] == 'CENTER'

    def test_can_set_line(self):
        termspark = TermSpark()
        assert termspark.line_is_set == False
        assert termspark.separator == ' ' # Default

        termspark.line()
        assert termspark.line_is_set == True
        assert termspark.separator == ' ' # Default

        termspark.line('.')
        assert termspark.line_is_set == True
        assert termspark.separator == '.'