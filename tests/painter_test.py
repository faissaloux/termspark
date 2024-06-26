from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight
from termspark.painter.painter import Painter


class TestPainter:
    def test_suffix(self):
        painter = Painter()
        assert painter.SUFFIX == "m"

    def test_reset(self):
        painter = Painter()
        assert painter.RESET == "\x1b[0m"

    def test_can_paint_existed_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("red")

        assert paint_color == f"{Fore.PREFIX}{Fore.RED}{painter.SUFFIX}"

    def test_can_paint_existed_multi_words_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("light_green")

        assert paint_color == f"{Fore.PREFIX}{Fore.LIGHT_GREEN}{painter.SUFFIX}"

    def test_return_empty_string_when_unexisted_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("unexisted")

        assert paint_color == ""

    def test_can_paint_existed_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("white")

        assert paint_highlight == f"{Highlight.PREFIX}{Highlight.WHITE}{painter.SUFFIX}"

    def test_can_paint_existed_multi_words_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("dark_blue")

        assert paint_highlight == f"{Highlight.PREFIX}{Highlight.DARK_BLUE}{painter.SUFFIX}"

    def test_return_empty_string_when_unexisted_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("unexisted")

        assert paint_highlight == ""

    def test_can_paint_rgb_color(self):
        painter = Painter()
        paint_color = painter.paint_color("255,22,200")

        assert paint_color == f"{Fore.RGB_PREFIX}255;22;200{painter.SUFFIX}"

    def test_paint_with_wrong_rgb_color(self):
        painter = Painter()
        paint_color = painter.paint_color("255,22,256")

        assert paint_color == ""

    def test_can_paint_rgb_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("255,22,200")

        assert paint_highlight == f"{Highlight.RGB_PREFIX}255;22;200{painter.SUFFIX}"

    def test_paint_with_wrong_rgb_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("255,22,256")

        assert paint_highlight == ""
