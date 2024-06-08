from termspark.painter.constants.color import Color
from termspark.painter.constants.highlight import Highlight


class TestHighlight:
    def test_prefix(self):
        assert Highlight.PREFIX == "\x1b[48;5;"

    def test_inherited_from_color(self):
        assert issubclass(Highlight, Color)
