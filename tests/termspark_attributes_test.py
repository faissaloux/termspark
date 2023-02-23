import pytest

from termspark import TermSpark
from termspark.exceptions.argCharsExceededException import ArgCharsExceededException


class TestTermsparkAttributes:
    def test_can_set_separator(self):
        termspark = TermSpark()
        assert termspark.separator == " "  # Default

        termspark.set_separator(".")
        assert termspark.separator == "."

    def test_cant_set_more_than_one_char_separator(self):
        termspark = TermSpark()
        assert termspark.separator == " "  # Default

        with pytest.raises(ArgCharsExceededException):
            termspark.set_separator("..")
        assert termspark.separator == " "  # Default

    def test_can_set_line(self):
        termspark = TermSpark()
        assert termspark.line_is_set == False
        assert termspark.separator == " "  # Default

        termspark.line()
        assert termspark.line_is_set == True
        assert termspark.separator == " "  # Default

        termspark.line(".")
        assert termspark.line_is_set == True
        assert termspark.separator == "."
