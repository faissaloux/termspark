from mock import patch  # type: ignore

from termspark.separator.separator import Separator


class TestSeparator:
    def test_init(self):
        data = {
            "content": ".",
            "color": "",
            "highlight": "",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        length = separator.get_length()

        assert separator.get_content() == "."
        assert separator.get_styled_content() == {
            "full": "." * length["full"],
            "left": "." * length["left"],
            "right": "." * length["right"],
        }

    def test_can_set_length(self):
        data = {
            "content": ".",
            "color": "",
            "highlight": "",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        separator.set_length(24)

        assert separator.get_length() == {
            "full": 24,
            "left": 12,
            "right": 12,
        }

    def test_can_set_odd_length(self):
        data = {
            "content": ".",
            "color": "",
            "highlight": "",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        separator.set_length(25)

        assert separator.get_length() == {
            "full": 25,
            "left": 13,
            "right": 12,
        }

    @patch("termspark.styler.styler.Styler.element")
    def test_style_call_styler_element(self, styler_element):
        data = {
            "content": ".",
            "color": "white",
            "highlight": "blue",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        separator.style()

        styler_element.assert_called_once_with(
            {
                "content": ["."],
                "color": ["white"],
                "highlight": ["blue"],
                "style": [""],
            }
        )

    @patch("termspark.styler.styler.Styler.style")
    def test_style_call_styler_style(self, styler_style):
        data = {
            "content": ".",
            "color": "white",
            "highlight": "blue",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        separator.style()

        styler_style.assert_called_once_with()

    def test_can_style(self):
        data = {
            "content": ".",
            "color": "white",
            "highlight": "blue",
            "style": "",
            "painted_content": ".",
            "styled_content": ".",
        }

        separator = Separator(data)
        separator.style()
        length = separator.get_length()

        assert separator.get_styled_content() == {
            "full": "\x1b[44m.\x1b[0m" * length["full"],
            "left": "\x1b[44m.\x1b[0m" * length["left"],
            "right": "\x1b[44m.\x1b[0m" * length["right"],
        }
