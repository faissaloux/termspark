from typing import List, Sequence, Union

from termspark.structurer.structurer import Form

from ..styler.styler import Styler


class Separator:
    __content: List[str]
    __color: List[str]
    __highlight: List[str]
    __painted_content: List[str]
    __style: List[Union[str, Sequence[str]]]
    __styled_content: List[str]
    __length: int

    def __init__(self, data: Form):
        self.__content = [data["content"]]
        self.__color = [data["color"]]
        self.__highlight = [data["highlight"]]
        self.__painted_content = [data["painted_content"]]
        self.__style = [data["style"]]
        self.__styled_content = [data["styled_content"]]

    def style(self):
        separator_data = dict(
            (key.replace("_Separator__", ""), value)
            for key, value in self.__dict__.items()
        )

        self.__styled_content = Styler().element(separator_data).style()

    def set_length(self, length: int) -> None:
        self.__length = length

    def get_content(self) -> str:
        return self.__content[0]

    def get_length(self) -> int:
        return self.__length

    def get_styled_content(self) -> str:
        return self.__styled_content[0]
