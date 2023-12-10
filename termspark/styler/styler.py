from typing import Final
from typing import List as ListType
from typing import Sequence

from typing_extensions import TypedDict

from ..helpers.list import List
from ..painter.painter import Painter
from ..text_styler.text_styler import TextStyler

Element = TypedDict(
    "Element",
    {
        "content": ListType[str],
        "encoded_content": ListType[str],
        "color": Sequence[str],
        "highlight": Sequence[str],
        "style": Sequence[Sequence[str]],
    },
)


class Styler:
    PATTERN: Final[str] = "[COLOR][HIGHLIGHT][STYLE][CONTENT][RESET]"
    RESET: Final[str] = "\x1b[0m"

    def __init__(self):
        self.styled: ListType[str] = []

    def element(self, element: Element):
        self.content = (
            element["encoded_content"]
            if "encoded_content" in element
            else element["content"]
        )
        self.content_color = element["color"]
        self.content_highlight = element["highlight"]
        self.content_style = element["style"]

        self.content_color = List().snake(self.content_color)
        self.content_highlight = List().snake(self.content_highlight)
        self.content_style = List().snake(self.content_style)

        return self

    def style(self) -> ListType[str]:
        for index, content in enumerate(self.content):
            self.styled.append(self.PATTERN)

            self.styled[-1] = self.styled[-1].replace(
                "[COLOR]", Painter().paint_color(self.content_color[index])
            )
            self.styled[-1] = self.styled[-1].replace(
                "[HIGHLIGHT]", Painter().paint_highlight(self.content_highlight[index])
            )
            self.styled[-1] = self.styled[-1].replace(
                "[STYLE]", TextStyler().style(self.content_style[index])
            )
            self.styled[-1] = self.styled[-1].replace("[CONTENT]", content)

            if any(
                [
                    len(self.content_color[index]),
                    len(self.content_highlight[index]),
                    len(self.content_style[index]),
                ]
            ):
                self.styled[-1] = self.styled[-1].replace("[RESET]", self.RESET)
            else:
                self.styled[-1] = self.styled[-1].replace("[RESET]", "")

        return self.styled
