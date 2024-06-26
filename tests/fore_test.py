from termspark.painter.constants.color import Color
from termspark.painter.constants.fore import Fore


class TestFore:
    def test_prefix(self):
        assert Fore.PREFIX == "\x1b[38;5;"

    def test_inherited_from_color(self):
        assert issubclass(Fore, Color)
