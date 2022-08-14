from termspark.painter.painter import Painter
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestPainter:
    def test_prefix(self):
        painter = Painter('content', 'red')
        assert painter.PREFIX == '\x1b['
    
    def test_suffix(self):
        painter = Painter('content', 'red')
        assert painter.SUFFIX == 'm'
    
    def test_reset(self):
        painter = Painter('content', 'red')
        assert painter.RESET == '\x1b[0m'

    def test_can_add_existed_fore_color(self):
        painter = Painter('content', 'red')

        assert painter.content == 'content'
        assert painter.color == 'red'
        assert painter.paint() == f'\x1b[{Fore.RED}mcontent\x1b[0m'

    def test_can_add_existed_multi_words_fore_color(self):
        painter = Painter('content', 'light red')

        assert painter.content == 'content'
        assert painter.color == 'light_red'
        assert painter.paint() == f'\x1b[{Fore.LIGHT_RED}mcontent\x1b[0m'

    def test_return_content_when_unexisted_fore_color(self):
        painter = Painter('content', 'pink')

        assert painter.content == 'content'
        assert painter.color == 'pink'
        assert painter.paint() == 'content'

    def test_can_add_existed_highlight(self):
        painter = Painter('content', None, 'blue')

        assert painter.content == 'content'
        assert painter.highlight == 'blue'
        assert painter.paint() == f'\x1b[{Highlight.BLUE}mcontent\x1b[0m'

    def test_can_add_existed_multi_words_highlight(self):
        painter = Painter('content', None, 'light red')

        assert painter.content == 'content'
        assert painter.highlight == 'light_red'
        assert painter.paint() == f'\x1b[{Highlight.LIGHT_RED}mcontent\x1b[0m'

    def test_return_content_when_unexisted_highlight(self):
        painter = Painter('content', None, 'pink')

        assert painter.content == 'content'
        assert painter.highlight == 'pink'
        assert painter.paint() == 'content'

    def test_can_add_existed_both_color_and_highlight(self):
        painter = Painter('content', 'red', 'blue')

        assert painter.content == 'content'
        assert painter.color == 'red'
        assert painter.highlight == 'blue'
        assert painter.paint() == f'\x1b[{Fore.RED}m\x1b[{Highlight.BLUE}mcontent\x1b[0m'

    def test_return_content_when_unexisted_both_color_and_highlight(self):
        painter = Painter('content', 'pink', 'beige')

        assert painter.content == 'content'
        assert painter.color == 'pink'
        assert painter.highlight == 'beige'
        assert painter.paint() == 'content'