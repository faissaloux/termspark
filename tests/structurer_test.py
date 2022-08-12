from termspark.structurer.structurer import Structurer
from termspark.painter.constants.fore import Fore

class TestStructurer:
    def test_structure_keys(self):
        structurer = Structurer('content').form()

        assert 'content' in structurer.keys()
        assert 'color' in structurer.keys()
        assert 'painted_content' in structurer.keys()

    def test_structure_without_color(self):
        structurer = Structurer('content').form()

        assert structurer.get('content') == 'content'
        assert structurer.get('color') == ''
        assert structurer.get('painted_content') == 'content'

    def test_structure_with_color(self):
        structurer = Structurer('content', 'red').form()

        assert structurer.get('content') == 'content'
        assert structurer.get('color') == 'red'
        assert structurer.get('painted_content') == f'\x1b[{Fore.RED}mcontent\x1b[0m'