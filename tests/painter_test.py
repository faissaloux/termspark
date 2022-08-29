from termspark.painter.painter import Painter
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestPainter:
    def test_prefix(self):
        painter = Painter()
        assert painter.PREFIX == '\x1b['
    
    def test_suffix(self):
        painter = Painter()
        assert painter.SUFFIX == 'm'
    
    def test_reset(self):
        painter = Painter()
        assert painter.RESET == '\x1b[0m'

    def test_attributes(self):
        position = {
            'content': 'content',
            'color': 'red',
            'highlight': ''
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['red']
        assert painter.highlight == ['']

    def test_mixed_styles_attributes(self):
        position = {
            'content': ['content1', 'content2'],
            'color': ['red', 'white'],
            'highlight': ['white', 'blue']
        }
        painter = Painter().position(position)

        assert painter.content == ['content1', 'content2']
        assert painter.color == ['red', 'white']
        assert painter.highlight == ['white', 'blue']

    def test_mixed_styles_missing_attributes(self):
        position = {
            'content': ['content1', 'content2'],
            'color': ['white', ''],
            'highlight': ['', 'blue']
        }
        painter = Painter().position(position)

        assert painter.content == ['content1', 'content2']
        assert painter.color == ['white', '']
        assert painter.highlight == ['', 'blue']

    def test_can_add_existed_fore_color(self):
        position = {
            'content': 'content',
            'color': 'red',
            'highlight': ''
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['red']
        assert painter.paint() == f'\x1b[{Fore.RED}mcontent\x1b[0m'

    def test_can_add_existed_multi_words_fore_color(self):
        position = {
            'content': 'content',
            'color': 'light red',
            'highlight': ''
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['light_red']
        assert painter.paint() == f'\x1b[{Fore.LIGHT_RED}mcontent\x1b[0m'

    def test_return_content_when_unexisted_fore_color(self):
        position = {
            'content': 'content',
            'color': 'pink',
            'highlight': ''
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['pink']
        assert painter.paint() == 'content'

    def test_can_add_existed_highlight(self):
        position = {
            'content': 'content',
            'color': None,
            'highlight': 'blue'
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.highlight == ['blue']
        assert painter.paint() == f'\x1b[{Highlight.BLUE}mcontent\x1b[0m'

    def test_can_add_existed_multi_words_highlight(self):
        position = {
            'content': 'content',
            'color': None,
            'highlight': 'light red'
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.highlight == ['light_red']
        assert painter.paint() == f'\x1b[{Highlight.LIGHT_RED}mcontent\x1b[0m'

    def test_return_content_when_unexisted_highlight(self):
        position = {
            'content': 'content',
            'color': None,
            'highlight': 'pink'
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.highlight == ['pink']
        assert painter.paint() == 'content'

    def test_can_add_existed_both_color_and_highlight(self):
        position = {
            'content': 'content',
            'color': 'red',
            'highlight': 'blue'
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['red']
        assert painter.highlight == ['blue']
        assert painter.paint() == f'\x1b[{Fore.RED}m\x1b[{Highlight.BLUE}mcontent\x1b[0m'

    def test_return_content_when_unexisted_both_color_and_highlight(self):
        position = {
            'content': 'content',
            'color': 'pink',
            'highlight': 'beige'
        }
        painter = Painter().position(position)

        assert painter.content == ['content']
        assert painter.color == ['pink']
        assert painter.highlight == ['beige']
        assert painter.paint() == 'content'