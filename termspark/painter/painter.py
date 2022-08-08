from .constants.fore import Fore

class Painter:
    PREFIX  = '\u001b['
    SUFFIX  = 'm'
    RESET   = '\u001b[0m'

    def __init__(self, content, color):
        self.content = content
        self.color = color

    def paint(self):
        return f"{self.PREFIX}{getattr(Fore, self.color.upper())}{self.SUFFIX}{self.content}{self.RESET}" if hasattr(Fore, self.color.upper()) else self.content