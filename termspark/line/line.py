from __future__ import annotations

from typing import (  # NotRequired can be moved here on Python >= 3.11.
    List,
    Sequence,
    TypedDict,
    Union,
)

from typing_extensions import NotRequired  # For Python <3.11.

from termspark.structurer.structurer import Form
from termspark.styler.styler import Styler

PositionedContent = TypedDict(
    "PositionedContent",
    {
        "full": str,
        "right": NotRequired[str],
        "left": NotRequired[str],
    },
)


class Line:
    _content: List[str]
    __color: List[str]
    __highlight: List[str]
    __painted_content: List[str]
    __style: List[Union[str, Sequence[str]]]
    _styled_content: List[str]

    def __init__(self, data: Form):
        self._content = [data["content"]]
        self.__color = [data["color"]]
        self.__highlight = [data["highlight"]]
        self.__painted_content = [data["painted_content"]]
        self.__style = [data["style"]]
        self._styled_content = [data["styled_content"]]

    def style(self):
        separator_data = {
            "content": self._content,
            "color": self.__color,
            "highlight": self.__highlight,
            "style": self.__style,
        }

        self._styled_content = Styler().element(separator_data).style()

    def get_content(self) -> str:
        return self._content[0]

    def get_styled_content(self) -> PositionedContent:
        return {
            "full": self._styled_content[0],
        }
