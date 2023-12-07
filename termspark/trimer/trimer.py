from typing import List


class Trimer:
    def __init__(self):
        self.to_trim: dict = {}

    def target(self, target: int):
        self.__chars_number_left = target

        return self

    def analyse(self, content: List[str], position: str) -> dict:
        self.to_trim[position] = {}

        for content_index in range(len(content) - 1, -1, -1):
            if self.__chars_number_left > 0:
                self.to_trim[position][content_index] = self.__analyse_single(
                    content[content_index]
                )

        return self.to_trim

    def should_be_trimed(self, position: str) -> bool:
        return position in self.to_trim and len(self.to_trim[position]) > 0

    def trim(self, content: List[str], position: str) -> List[str]:
        for index, to_trim in self.to_trim[position].items():
            content[index] = "".join(content[index].rsplit(to_trim, 1))

        return content

    def __analyse_single(self, content: str) -> str:
        to_trim: str = ""

        if len(content) > self.__chars_number_left:
            to_trim = content[len(content) - self.__chars_number_left :]
            self.__chars_number_left -= self.__chars_number_left
        else:
            to_trim = content
            self.__chars_number_left = self.__chars_number_left - len(content)

        return to_trim
