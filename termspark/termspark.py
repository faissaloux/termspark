import os
from itertools import chain
from .structurer.structurer import Structurer
from .helpers.existenceChecker import ExistenceChecker
from .exceptions.printerArgException import PrinterArgException
from .exceptions.argCharsExceededException import ArgCharsExceededException

class TermSpark:
    left = {}
    right = {}
    center = {}
    separator = ' '
    line_is_set = False
    positions = [
        'left',
        'right',
        'center',
    ]
    colors = chain(range(30, 37), range(90, 97))
    highlights = chain(range(41, 47), range(100, 108))
    attributes = range(1, 9)

    design_codes = []

    def __init__(self):
        self.set_design_codes()

    def print_left(self, content, color = None, highlight = None):
        self.print_position('left', content, color, highlight)

        return self

    def print_right(self, content, color = None, highlight = None):
        self.print_position('right', content, color, highlight)

        return self

    def print_center(self, content, color = None, highlight = None):
        self.print_position('center', content, color, highlight)

        return self

    def spark_left(self, *contents):
        self.spark_position('left', *contents)

        return self

    def spark_right(self, *contents):
        self.spark_position('right', *contents)

        return self

    def spark_center(self, *contents):
        self.spark_position('center', *contents)

        return self

    def print_position(self, position, content, color, highlight):
        if isinstance(content, list): raise PrinterArgException(position)
        positionContent = Structurer(content, color, highlight).form()

        setattr(self, position, positionContent)

    def spark_position(self, position, *contents):
        positionContent = getattr(self, position) if getattr(self, position) else {}

        if (isinstance(contents[0], list)):
            for content in contents:
                if not positionContent:
                    positionContent = Structurer(*content).form()
                else:
                    positionContent['painted_content'] += Structurer(*content).form()['painted_content']
        else:
            if not positionContent:
                positionContent = Structurer(*contents).form()
            else:
                positionContent['painted_content'] += Structurer(*contents).form()['painted_content']

        setattr(self, position, positionContent)

    def set_separator(self, separator):
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

    def calculate_colors_codes_length(self):
        colors_codes_length = 0

        for design_code in self.design_codes:
            for position in self.positions:
                position_content = ExistenceChecker().dictionary_key(getattr(self, position), 'painted_content')
                if design_code in position_content:
                    colors_codes_length += (len(design_code) * position_content.count(design_code)) + position_content.count(design_code)

        return colors_codes_length - len('\x1b')

    def line(self, separator = None):
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

    def get_terminal_width(self):
        try:
            width = os.get_terminal_size()[0]
        except OSError:
            width = 80
        return width

    def render(self):
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

    def spark(self):
        print(self.render())

    def __repr__(self):
        return self.render()