from ..painter.painter import Painter

class Structurer:
    def __init__(self, content, color = None, highlight = None):
        self.content = content
        self.color = color
        self.highlight = highlight

    def form(self):
        return {
            'content': self.content if self.content else '',
            'color': self.color if self.color else '',
            'highlight': self.highlight if self.highlight else '',
            'painted_content': Painter(self.content, self.color, self.highlight).paint() if self.color or self.highlight else self.content,
        }

