import pytest
from mock import patch  # type: ignore

from termspark.exceptions.len_not_supported_error import LenNotSupportedError
from termspark.termspark import TermSpark


class TestTermspark:
    def test_cant_set_more_empty_char_separator(self):
        with pytest.raises(LenNotSupportedError):
            TermSpark().set_separator("")

    def test_cant_set_more_than_one_char_separator(self):
        with pytest.raises(LenNotSupportedError):
            TermSpark().set_separator("..")

    @patch("termspark.separator.separator.Separator.__init__")
    def test_can_set_separator_with_only_content(self, separator):
        separator.return_value = None
        TermSpark().set_separator(".")

        separator.assert_called_with(
            {
                "content": ".",
                "color": "",
                "highlight": "",
                "style": "",
                "styled_content": ".",
            }
        )

    @patch("termspark.separator.separator.Separator.__init__")
    def test_can_set_separator_with_color(self, separator):
        separator.return_value = None
        TermSpark().set_separator(".", "white")

        separator.assert_called_with(
            {
                "content": ".",
                "color": "white",
                "highlight": "",
                "style": "",
                "styled_content": ".",
            }
        )

    @patch("termspark.separator.separator.Separator.__init__")
    def test_can_set_separator_with_color_and_highlight(self, separator):
        separator.return_value = None
        TermSpark().set_separator(".", "white", "blue")

        separator.assert_called_with(
            {
                "content": ".",
                "color": "white",
                "highlight": "blue",
                "style": "",
                "styled_content": ".",
            }
        )
