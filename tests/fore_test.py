from termspark.painter.constants.fore import Fore

class TestFore:
    def test_black(self):
        assert Fore.BLACK == 30

    def test_red(self):
        assert Fore.RED == 31

    def test_green(self):
        assert Fore.GREEN == 32

    def test_yellow(self):
        assert Fore.YELLOW == 33

    def test_blue(self):
        assert Fore.BLUE == 34

    def test_magenta(self):
        assert Fore.MAGENTA == 35

    def test_cyan(self):
        assert Fore.CYAN == 36

    def test_gray(self):
        assert Fore.GRAY == 90

    def test_grey(self):
        assert Fore.GREY == 90

    def test_light_red(self):
        assert Fore.LIGHT_RED == 91

    def test_light_green(self):
        assert Fore.LIGHT_GREEN == 92

    def test_light_yellow(self):
        assert Fore.LIGHT_YELLOW == 93

    def test_light_blue(self):
        assert Fore.LIGHT_BLUE == 94

    def test_light_magenta(self):
        assert Fore.LIGHT_MAGENTA == 95

    def test_light_cyan(self):
        assert Fore.LIGHT_CYAN == 96