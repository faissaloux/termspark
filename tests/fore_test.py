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

    def test_white(self):
        assert Fore.WHITE == 37