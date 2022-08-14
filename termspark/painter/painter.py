from .constants.fore import Fore
from .constants.highlight import Highlight

class Painter:
    PREFIX  = '\x1b['
    SUFFIX  = 'm'
    RESET   = '\x1b[0m'

    def __init__(self, content, color = None, highlight = None):
        self.content = content
        self.color = color.replace(' ', '_') if color else color
        self.highlight = highlight.replace(' ', '_') if highlight else highlight

    def paint(self):
        return f"{self.paint_color()}{self.paint_highlight()}{self.content}{self.reset()}"

    def paint_color(self):
        if self.color and hasattr(Fore, self.color.upper()):
            return f"{self.PREFIX}{getattr(Fore, self.color.upper())}{self.SUFFIX}"
        return ''

    def paint_highlight(self):
        if self.highlight and hasattr(Highlight, self.highlight.upper()):
            return f"{self.PREFIX}{getattr(Highlight, self.highlight.upper())}{self.SUFFIX}"
        return ''

    def reset(self):
        if (self.color and hasattr(Fore, self.color.upper())) or (self.highlight and hasattr(Highlight, self.highlight.upper())):
            return self.RESET
        else:
            return ''
