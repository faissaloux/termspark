from termspark import TermSpark
from termspark.painter.constants.fore import Fore
from termspark.painter.constants.highlight import Highlight

class TestTermsparkColors:
    def test_one_color_code_length_calculation(self):
        termspark = TermSpark().print_left('LEFT', 'red')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm' + '\x1b[0m') - len('\x1b')

    def test_multiple_colors_code_length_calculation(self):
        termspark = TermSpark().print_left('LEFT', 'red').print_right('RIGHT', 'blue')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm' + '\x1b[0m') + len('\x1b[' + str(Fore.BLUE) + 'm') + len('\x1b[0m') - len('\x1b')

    def test_multiple_colors_and_highlights_code_length_calculation(self):
        termspark = TermSpark().print_left('LEFT', 'red', 'white').print_right('RIGHT', 'white', 'blue')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm') + len('\x1b[' + str(Highlight.WHITE) + 'm') + len('\x1b[0m') + len('\x1b[' + str(Highlight.BLUE) + 'm') + len('\x1b[0m') - len('\x1b')

    def test_spark_one_content(self):
        termspark = TermSpark().spark_left('LEFT', 'red', 'white')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm') + len('\x1b[' + str(Highlight.WHITE) + 'm') + len('\x1b[0m') - len('\x1b')

    def test_spark_support_one_content_list(self):
        termspark = TermSpark().spark_right(['RIGHT', 'red', 'white'])
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm') + len('\x1b[' + str(Highlight.WHITE) + 'm') + len('\x1b[0m') - len('\x1b')

    def test_spark_support_multiple_content_lists(self):
        termspark = TermSpark().spark_center(['CENTER', 'red', 'white'], ['CENTER', 'white', 'magenta'])
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm') + len('\x1b[' + str(Highlight.WHITE) + 'm') + len('\x1b[0m') + len('\x1b[' + str(Highlight.MAGENTA) + 'm') + len('\x1b[0m') - len('\x1b')

    def test_can_chain_multiple_same_position_spark(self):
        termspark = TermSpark()
        termspark.spark_left([' * ', 'black', 'white'])
        termspark.spark_left([' LEFT ', 'white', 'red'])
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.BLACK) + 'm') + len('\x1b[' + str(Highlight.WHITE) + 'm') + len('\x1b[0m') + len('\x1b[' + str(Highlight.RED) + 'm') + len('\x1b[0m') - len('\x1b')