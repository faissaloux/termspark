from typing import List


class Trimer:
    def target(self, target: int):
        self.__chars_number_left = target

        return self

    def analyse(self, content: List[str]) -> dict:
        to_trim: dict = {}

        for content_index in range(len(content) - 1, -1, -1):
            if self.__chars_number_left > 0:
                to_trim[content_index] = self.__analyse_single(content[content_index])

        return to_trim

    def __analyse_single(self, content: str) -> str:
        to_trim: str = ""

        if len(content) > self.__chars_number_left:
            to_trim = content[len(content) - self.__chars_number_left :]
            self.__chars_number_left -= self.__chars_number_left
        else:
            to_trim = content
            self.__chars_number_left = self.__chars_number_left - len(content)

        return to_trim
