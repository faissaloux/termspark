import os

class TermSpark:
    left = ''
    right = ''
    center = ''
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

    def print_left(self, string):
        self.left = string

        return self

    def print_right(self, string):
        self.right = string

        return self

    def print_center(self, string):
        self.center = string

        return self

    def set_separator(self, separator):
        if len(separator) > 1: raise Exception("Sorry, separator must contain only one character") 
        self.separator = separator

        return self

    def calculate_separator_length(self):
        colors_codes_length = self.calculate_colors_codes_length()
        content_length = 0

        for placement in self.placements:
            content_length += len(getattr(self, placement))
        self.separator_length = os.get_terminal_size()[0] - content_length + colors_codes_length

    def calculate_colors_codes_length(self):
        colors_codes_length = 0

        for design_code in self.design_codes:
            for placement in self.placements:
                placement_content = getattr(self, placement)
                if design_code in placement_content:
                    colors_codes_length += (len(design_code) * placement_content.count(design_code)) + placement_content.count(design_code)

        return colors_codes_length

    def line(self, separator = None):
        self.line_is_set = True
        self.set_separator(separator)

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

    def __del__(self):
        self.calculate_separator_length()
        separator_mid_width = self.separator * int( self.separator_length / 2 )

        if self.left or self.right or self.center or self.line_is_set:
            if self.center:
                center = separator_mid_width + self.center + separator_mid_width
            else:
                center = self.separator * self.separator_length
            print(self.left + center + self.right)