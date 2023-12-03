from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight
from termspark.painter.painter import Painter


class TestPainter:
    def test_prefix(self):
        painter = Painter()
        assert painter.PREFIX == "\x1b["

    def test_suffix(self):
        painter = Painter()
        assert painter.SUFFIX == "m"

    def test_reset(self):
        painter = Painter()
        assert painter.RESET == "\x1b[0m"

    def test_can_paint_existed_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("red")

        assert paint_color == f"{painter.PREFIX}{Fore.RED}{painter.SUFFIX}"

    def test_can_paint_existed_multi_words_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("light_green")

        assert paint_color == f"{painter.PREFIX}{Fore.LIGHT_GREEN}{painter.SUFFIX}"

    def test_return_empty_string_when_unexisted_fore_color(self):
        painter = Painter()
        paint_color = painter.paint_color("unexisted")

        assert paint_color == ""

    def test_can_paint_existed_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("white")

        assert paint_highlight == f"{painter.PREFIX}{Highlight.WHITE}{painter.SUFFIX}"

    def test_can_paint_existed_multi_words_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("light_blue")

        assert (
            paint_highlight == f"{painter.PREFIX}{Highlight.LIGHT_BLUE}{painter.SUFFIX}"
        )

    def test_return_empty_string_when_unexisted_highlight(self):
        painter = Painter()
        paint_highlight = painter.paint_highlight("unexisted")

        assert paint_highlight == ""
