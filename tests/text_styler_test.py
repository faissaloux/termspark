from termspark.text_styler.constants.style import Style
from termspark.text_styler.text_styler import TextStyler


class TestTextStyler:
    def test_prefix(self):
        assert TextStyler.PREFIX == "\x1b["

    def test_suffix(self):
        assert TextStyler.SUFFIX == "m"

    def test_existed_style(self):
        text_styler = TextStyler()
        style = text_styler.style(["bold", "italic"])

        assert (
            style
            == f"{text_styler.PREFIX}{Style.BOLD}{text_styler.SUFFIX}{text_styler.PREFIX}{Style.ITALIC}{text_styler.SUFFIX}"
        )

    def test_unexisted_style(self):
        text_styler = TextStyler()
        style = text_styler.style(["unexisted"])

        assert style == ""

    def test_existed_with_unexisted_style(self):
        text_styler = TextStyler()
        style = text_styler.style(["bold", "unexisted"])

        assert style == f"{text_styler.PREFIX}{Style.BOLD}{text_styler.SUFFIX}"
