import os
from .structurer.structurer import Structurer
import colorama

colorama.init()

class TermSpark:
    left = {
        'content': '',
        'color': '',
        'painted_content': '',
    }
    right = {
        'content': '',
        'color': '',
        'painted_content': '',
    }
    center = {
        'content': '',
        'color': '',
        'painted_content': '',
    }
    separator = ' '
    line_is_set = False
    placements = [
        'left',
        'right',
        'center',
    ]
    colors = range(30, 37)
    highlights = range(40, 48)
    attributes = range(1, 9)

    design_codes = []

    def __init__(self):
        self.set_design_codes()

    def print_left(self, content, color = None):
        self.left = Structurer(content, color).form()

        return self

    def print_right(self, content, color = None):
        self.right = Structurer(content, color).form()

        return self

    def print_center(self, content, color = None):
        self.center = Structurer(content, color).form()

        return self

    def set_separator(self, separator):
        if len(separator) > 1: raise Exception("Sorry, separator can contain only one character") 
        self.separator = separator

        return self

    def calculate_separator_length(self):
        colors_codes_length = self.calculate_colors_codes_length()
        content_length = 0

        for placement in self.placements:
            content_length += len(getattr(self, placement)['painted_content'])
        self.separator_length = self.get_terminal_width() - content_length + colors_codes_length

    def calculate_colors_codes_length(self):
        colors_codes_length = 0

        for design_code in self.design_codes:
            for placement in self.placements:
                placement_content = getattr(self, placement)['painted_content']
                if design_code in placement_content:
                    colors_codes_length += (len(design_code) * placement_content.count(design_code)) + placement_content.count(design_code)

        return colors_codes_length - len('\u001b')

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

    def __del__(self):
        self.calculate_separator_length()
        separator_mid_width = self.separator * int( self.separator_length / 2 )

        if 'content' in self.left or 'content' in self.right or 'content' in self.center or self.line_is_set:
            if len(self.center['content']) > 0:
                center = separator_mid_width + self.center['painted_content'] + separator_mid_width
            else:
                center = self.separator * self.separator_length

            print(self.left['painted_content'] + center + self.right['painted_content'])