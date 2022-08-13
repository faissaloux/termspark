from termspark.painter.constants.highlight import Highlight

class TestHighlight:
    def test_red(self):
        assert Highlight.RED == 41

    def test_green(self):
        assert Highlight.GREEN == 42

    def test_yellow(self):
        assert Highlight.YELLOW == 43

    def test_blue(self):
        assert Highlight.BLUE == 44

    def test_magenta(self):
        assert Highlight.MAGENTA == 45

    def test_cyan(self):
        assert Highlight.CYAN == 46

    def test_white(self):
        assert Highlight.WHITE == 47