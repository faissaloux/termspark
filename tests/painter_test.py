from termspark.painter.painter import Painter
from termspark.painter.constants.fore import Fore

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

    def test_return_content_when_unexisted_fore_color(self):
        painter = Painter('content', 'pink')

        assert painter.content == 'content'
        assert painter.color == 'pink'
        assert painter.paint() == 'content'