from ..painter.painter import Painter

class Structurer:
    def __init__(self, content, color = None):
        self.content = content
        self.color = color

    def form(self):
        return {
            'content': self.content if self.content else '',
            'color': self.color if self.color else '',
            'painted_content': Painter(self.content, self.color).paint() if self.color else self.content,
        }

