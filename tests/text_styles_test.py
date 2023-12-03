from termspark.text_styler.constants.style import Style


class TestTextStyles:
    def test_bold(self):
        assert Style.BOLD == 1

    def test_dim(self):
        assert Style.DIM == 2

    def test_italic(self):
        assert Style.ITALIC == 3

    def test_underline(self):
        assert Style.UNDERLINE == 4

    def test_blink(self):
        assert Style.BLINK == 5

    def test_reverse(self):
        assert Style.REVERSE == 7

    def test_hidden(self):
        assert Style.HIDDEN == 8

    def test_strike_through(self):
        assert Style.STRIKE_THROUGH == 9

    def test_double_underline(self):
        assert Style.DOUBLE_UNDERLINE == 21

    def test_overline(self):
        assert Style.OVERLINE == 53
