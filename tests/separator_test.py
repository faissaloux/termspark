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

        assert separator.get_content() == "."
        assert separator.get_styled_content() == "."

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
        separator.set_length(6)

        assert separator.get_length() == 6

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

        assert separator.get_styled_content() == "\x1b[44m.\x1b[0m"
