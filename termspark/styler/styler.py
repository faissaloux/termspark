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
    PATTERN = "[COLOR][HIGHLIGHT][STYLE][CONTENT][RESET]"
    RESET: str = "\x1b[0m"

    styled: str = ""

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

    def style(self) -> str:
        for index, content in enumerate(self.content):
            self.styled = self.styled + self.PATTERN
            self.styled = self.styled.replace(
                "[COLOR]", Painter().paint_color(self.content_color[index])
            )
            self.styled = self.styled.replace(
                "[HIGHLIGHT]", Painter().paint_highlight(self.content_highlight[index])
            )
            self.styled = self.styled.replace(
                "[STYLE]", TextStyler().style(self.content_style[index])
            )
            self.styled = self.styled.replace("[CONTENT]", content)

            if any(
                [
                    len(self.content_color[index]),
                    len(self.content_highlight[index]),
                    len(self.content_style[index]),
                ]
            ):
                self.styled = self.styled.replace("[RESET]", self.RESET)
            else:
                self.styled = self.styled.replace("[RESET]", "")

        return self.styled
