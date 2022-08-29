from .constants.fore import Fore
from .constants.highlight import Highlight
from ..helpers.list import List

class Painter:
    painted = ''
    PREFIX  = '\x1b['
    SUFFIX  = 'm'
    RESET   = '\x1b[0m'

    def position(self, position):
        self.content = position['content'] if isinstance(position['content'], list) else [position['content']]
        self.color = position['color'] if isinstance(position['color'], list) else [position['color']]
        self.highlight = position['highlight'] if isinstance(position['highlight'], list) else [position['highlight']]

        self.color = List().snake(self.color)
        self.highlight = List().snake(self.highlight)
        return self

    def paint(self):
        for index, content in enumerate(self.content):
            self.painted += f"{self.paint_color(self.color[index])}{self.paint_highlight(self.highlight[index])}{content}{self.reset(self.color[index], self.highlight[index])}"

        return self.painted

    def paint_color(self, color):
        if color and hasattr(Fore, color.upper()):
            return f"{self.PREFIX}{getattr(Fore, color.upper())}{self.SUFFIX}"
        return ''

    def paint_highlight(self, highlight):
        if highlight and hasattr(Highlight, highlight.upper()):
            return f"{self.PREFIX}{getattr(Highlight, highlight.upper())}{self.SUFFIX}"
        return ''

    def reset(self, color, highlight):
        if (color and hasattr(Fore, color.upper())) or (highlight and hasattr(Highlight, highlight.upper())):
            return self.RESET
        else:
            return ''
