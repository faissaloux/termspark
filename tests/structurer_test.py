from termspark.structurer.structurer import Structurer
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestStructurer:
    def test_structure_keys(self):
        structurer = Structurer('content').form()

        assert 'content' in structurer.keys()
        assert 'color' in structurer.keys()
        assert 'highlight' in structurer.keys()
        assert 'painted_content' in structurer.keys()

    def test_structure_without_both_color_and_highlight(self):
        structurer = Structurer('content').form()

        assert structurer.get('content') == 'content'
        assert structurer.get('color') == ''
        assert structurer.get('highlight') == ''
        assert structurer.get('painted_content') == 'content'

    def test_structure_with_color(self):
        structurer = Structurer('content', 'red').form()

        assert structurer.get('content') == 'content'
        assert structurer.get('color') == 'red'
        assert structurer.get('highlight') == ''
        assert structurer.get('painted_content') == f'\x1b[{Fore.RED}mcontent\x1b[0m'

    def test_structure_with_both_color_and_highlight(self):
        structurer = Structurer('content', 'red', 'yellow').form()

        assert structurer.get('content') == 'content'
        assert structurer.get('color') == 'red'
        assert structurer.get('highlight') == 'yellow'
        assert structurer.get('painted_content') == f'\x1b[{Fore.RED}m\x1b[{Highlight.YELLOW}mcontent\x1b[0m'