from termspark import TermSpark
from termspark.painter.constants.fore import Fore

class TestTermsparkColors:
    def test_one_color_code_length_calculation(self):
        termspark = TermSpark().print_left('LEFT', 'red')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm' + '\x1b[0m')  - len('\x1b')

    def test_multiple_colors_code_length_calculation(self):
        termspark = TermSpark().print_left('LEFT', 'red').print_right('RIGHT', 'blue')
        color_code_length = termspark.calculate_colors_codes_length()

        assert color_code_length == len('\x1b[' + str(Fore.RED) + 'm' + '\x1b[0m') + len('\x1b[' + str(Fore.BLUE) + 'm' + '\x1b[0m') - len('\x1b')
