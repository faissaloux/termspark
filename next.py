
def trim(self, chars_number):
    self.positions.reverse()
    chars_number_left = chars_number
    for position in self.positions:
        new_content = []
        if 'content' in getattr(self, position).keys():
            if isinstance(getattr(self, position)['content'], list):
                getattr(self, position)['content'].reverse()
                for index, content in enumerate(getattr(self, position)['content']):
                    new_content.append(content[0:len(content) - chars_number_left])
                    chars_number_left -= chars_number

                getattr(self, position)['content'] = new_content
            else:
                content = getattr(self, position)['content']
                new_content.append(content[0:len(content) - chars_number_left])
                chars_number_left -= chars_number
                getattr(self, position)['content'] = new_content

            getattr(self, position)['content'].reverse()
    self.positions.reverse()
    print(self.render())


def spark(self):
        render = self.render()
        to_trim = len(render) - self.get_terminal_width() - 47

        if to_trim > 0 :
            self.trim(to_trim)
        else:
            print(render)