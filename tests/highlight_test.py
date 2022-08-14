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

    def test_gray(self):
        assert Highlight.GRAY == 100

    def test_light_red(self):
        assert Highlight.LIGHT_RED == 101

    def test_light_green(self):
        assert Highlight.LIGHT_GREEN == 102

    def test_light_yellow(self):
        assert Highlight.LIGHT_YELLOW == 103

    def test_light_blue(self):
        assert Highlight.LIGHT_BLUE == 104

    def test_light_magenta(self):
        assert Highlight.LIGHT_MAGENTA == 105

    def test_light_cyan(self):
        assert Highlight.LIGHT_CYAN == 106

    def test_white(self):
        assert Highlight.WHITE == 107