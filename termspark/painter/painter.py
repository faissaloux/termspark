from typing import Dict
from typing import List as ListType
from typing import Union

from ..helpers.list import List
from .constants.fore import Fore
from .constants.highlight import Highlight


class Painter:
    painted: str = ""
    PREFIX: str = "\x1b["
    SUFFIX: str = "m"
    RESET: str = "\x1b[0m"

    def position(self, position: Dict[str, Union[str, ListType[str]]]):
        self.content = (
            position["content"]
            if isinstance(position["content"], list)
            else [position["content"]]
        )
        self.color = (
            position["color"]
            if isinstance(position["color"], list)
            else [position["color"]]
        )
        self.highlight = (
            position["highlight"]
            if isinstance(position["highlight"], list)
            else [position["highlight"]]
        )

        self.color = List().snake(self.color)
        self.highlight = List().snake(self.highlight)

        return self

    def paint(self) -> str:
        for index, content in enumerate(self.content):
            self.painted += f"{self.paint_color(self.color[index])}{self.paint_highlight(self.highlight[index])}{content}{self.reset(self.color[index], self.highlight[index])}"

        return self.painted

    def paint_color(self, color: str) -> str:
        if color and hasattr(Fore, color.upper()):
            return f"{self.PREFIX}{getattr(Fore, color.upper())}{self.SUFFIX}"
        return ""

    def paint_highlight(self, highlight: str) -> str:
        if highlight and hasattr(Highlight, highlight.upper()):
            return f"{self.PREFIX}{getattr(Highlight, highlight.upper())}{self.SUFFIX}"
        return ""

    def reset(self, color: str, highlight: str) -> str:
        if (color and hasattr(Fore, color.upper())) or (
            highlight and hasattr(Highlight, highlight.upper())
        ):
            return self.RESET
        else:
            return ""
