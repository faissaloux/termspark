import os
from itertools import chain
from typing import Optional, Dict, List
from .structurer.structurer import Structurer
from .painter.painter import Painter
from .helpers.existenceChecker import ExistenceChecker
from .exceptions.printerArgException import PrinterArgException
from .exceptions.argCharsExceededException import ArgCharsExceededException
from .exceptions.printerSparkerMixException import PrinterSparkerMixException

class TermSpark:
    left: Dict[str, str] = {}
    right: Dict[str, str] = {}
    center: Dict[str, str] = {}
    separator: str = ' '
    line_is_set: bool = False
    printed: List[str] = []
    colors: chain = chain(range(30, 37), range(90, 97))
    highlights: chain = chain(range(41, 47), range(100, 108))
    attributes: range = range(1, 9)
    design_codes: List[str] = []
    positions: List[str] = [
        'left',
        'center',
        'right',
    ]

    def __init__(self):
        self.set_design_codes()
        self.printed = []

    def print_left(self, content: str, color: Optional[str] = None, highlight: Optional[str] = None):
        self.print_position('left', content, color, highlight)

        return self

    def print_right(self, content: str, color: Optional[str] = None, highlight: Optional[str] = None):
        self.print_position('right', content, color, highlight)

        return self

    def print_center(self, content: str, color: Optional[str] = None, highlight: Optional[str] = None):
        self.print_position('center', content, color, highlight)

        return self

    def spark_left(self, *contents: List[str]):
        self.spark_position('left', *contents)

        return self

    def spark_right(self, *contents: List[str]):
        self.spark_position('right', *contents)

        return self

    def spark_center(self, *contents: List[str]):
        self.spark_position('center', *contents)

        return self

    def print_position(self, position: str, content: str, color: Optional[str], highlight: Optional[str]):
        if isinstance(content, list): raise PrinterArgException(position)
        positionContent = Structurer(content, color, highlight).form()
        self.printed.append(position)

        setattr(self, position, positionContent)

    def spark_position(self, position: str, *contents: List[str]):
        if position in self.printed: raise PrinterSparkerMixException(position)
        positionContent = getattr(self, position) if getattr(self, position) else {}

        if (isinstance(contents[0], list)):
            for content in contents:
                positionContent = self.appendPositionContent(positionContent, *content)
        else:
            positionContent = self.appendPositionContent(positionContent, *contents)

        setattr(self, position, positionContent)

    def appendPositionContent(self, positionContent: Dict[str, List[str]], *content: str):
        if not positionContent:
            positionContent['content'] = [Structurer(*content).form()['content']]
            positionContent['color'] = [Structurer(*content).form()['color']]
            positionContent['highlight'] = [Structurer(*content).form()['highlight']]
        else:
            positionContent['content'].append(Structurer(*content).form()['content'])
            positionContent['color'].append(Structurer(*content).form()['color'])
            positionContent['highlight'].append(Structurer(*content).form()['highlight'])

        return positionContent

    def set_separator(self, separator: str):
        if len(separator) > 1: raise ArgCharsExceededException('separator', 'one')
        self.separator = separator

        return self

    def calculate_separator_length(self):
        colors_codes_length = self.calculate_colors_codes_length()
        content_length = 0

        for position in self.positions:
            painted_content = ExistenceChecker().dictionary_key(getattr(self, position), 'painted_content')
            content_length += len(painted_content)
        self.separator_length = self.get_terminal_width() - content_length + colors_codes_length

    def calculate_colors_codes_length(self) -> int:
        colors_codes_length = 0

        for design_code in self.design_codes:
            for position in self.positions:
                position_content = ExistenceChecker().dictionary_key(getattr(self, position), 'painted_content')
                if design_code in position_content:
                    colors_codes_length += (len(design_code) * position_content.count(design_code)) + position_content.count(design_code)

        return colors_codes_length - len('\x1b')

    def line(self, separator: Optional[str] = None):
        self.line_is_set = True
        self.set_separator(separator if separator else self.separator)

        return self

    def set_design_codes(self):
        for color in self.colors:
            if f'[{color}m' not in self.design_codes:
                self.design_codes.append(f'[{color}m')
        for highlight in self.highlights:
            if f'[{highlight}m' not in self.design_codes:
                self.design_codes.append(f'[{highlight}m')
        for attribute in self.attributes:
            if f'[{attribute}m' not in self.design_codes:
                self.design_codes.append(f'[{attribute}m')

        if f'[0m' not in self.design_codes:
            self.design_codes.append('[0m')

    def get_terminal_width(self) -> int:
        try:
            width = os.get_terminal_size()[0]
        except OSError:
            width = 80
        return width

    def render(self) -> str:
        self.paint_content()
        self.calculate_separator_length()
        separator_mid_width = self.separator * int( self.separator_length / 2 )

        if 'content' in self.left or 'content' in self.right or 'content' in self.center or self.line_is_set:
            center_content = ExistenceChecker().dictionary_key(self.center, 'content')
            if len( center_content ) > 0:
                center = separator_mid_width + self.center['painted_content'] + separator_mid_width
            else:
                center = self.separator * self.separator_length

            left_painted_content = ExistenceChecker().dictionary_key(self.left, 'painted_content')
            right_painted_content = ExistenceChecker().dictionary_key(self.right, 'painted_content')

        return left_painted_content + center + right_painted_content

    def paint_content(self):
        for position in self.positions:
            pos = getattr(self, position) if getattr(self, position) else {}
            if pos:
                pos['painted_content'] = Painter().position(pos).paint()

            setattr(self, position, pos)

    def spark(self):
        print(self.render())

    def __repr__(self) -> str:
        return self.render()