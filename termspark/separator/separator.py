from typing import TypedDict

from typing_extensions import override

from termspark.line.line import Line, PositionedContent
from termspark.structurer.structurer import Form

Length = TypedDict(
    "Length",
    {
        "full": int,
        "right": int,
        "left": int,
    },
)


class Separator(Line):
    __length: Length = {
        "full": 0,
        "right": 0,
        "left": 0,
    }

    def __init__(self, data: Form):
        super().__init__(data)

    def set_length(self, length: int) -> None:
        half_separator_length = length // 2
        half_left_separator_length = half_separator_length

        if length % 2 != 0:
            half_left_separator_length += 1

        self.__length = {
            "full": length,
            "left": half_left_separator_length,
            "right": half_separator_length,
        }

    def get_length(self) -> Length:
        return self.__length

    @override
    def get_raw_content(self) -> PositionedContent:
        return {
            "full": self._content[0] * self.__length["full"],
            "left": self._content[0] * self.__length["left"],
            "right": self._content[0] * self.__length["right"],
        }

    @override
    def get_styled_content(self) -> PositionedContent:
        return {
            "full": self._styled_content[0] * self.__length["full"],
            "left": self._styled_content[0] * self.__length["left"],
            "right": self._styled_content[0] * self.__length["right"],
        }
