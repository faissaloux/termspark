import pytest

from termspark.exceptions.argCharsExceededException import ArgCharsExceededException
from termspark.termspark import TermSpark


class TestTermsparkAttributes:
    def test_can_set_separator_content(self):
        termspark = TermSpark()
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.set_separator(".")
        assert termspark.separator["content"] == "."
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

    def test_cant_set_more_than_one_char_separator(self):
        termspark = TermSpark()
        assert termspark.separator["content"] == " "  # Default

        with pytest.raises(ArgCharsExceededException):
            termspark.set_separator("..")
        assert termspark.separator["content"] == " "  # Default

    def test_can_set_separator_with_color(self):
        termspark = TermSpark()
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.set_separator(".", "blue")
        assert termspark.separator["content"] == "."
        assert termspark.separator["color"] == "blue"
        assert termspark.separator["highlight"] == ""

    def test_can_set_separator_with_color_and_highlight(self):
        termspark = TermSpark()
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.set_separator(".", "green", "yellow")
        assert termspark.separator["content"] == "."
        assert termspark.separator["color"] == "green"
        assert termspark.separator["highlight"] == "yellow"

    def test_can_set_line(self):
        termspark = TermSpark()
        assert termspark.line_is_set == False
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.line()
        assert termspark.line_is_set == True
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.line(".")
        assert termspark.line_is_set == True
        assert termspark.separator["content"] == "."
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

    def test_can_set_line_with_highlight(self):
        termspark = TermSpark()
        assert termspark.line_is_set == False
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == ""  # Default

        termspark.line(highlight="green")
        assert termspark.line_is_set == True
        assert termspark.separator["content"] == " "  # Default
        assert termspark.separator["color"] == ""  # Default
        assert termspark.separator["highlight"] == "green"
