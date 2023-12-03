from typing import Optional, Sequence

from typing_extensions import TypedDict

Form = TypedDict(
    "Form",
    {
        "content": str,
        "color": str,
        "highlight": str,
        "style": Sequence[str],
        "painted_content": str,
        "styled_content": str,
    },
)


class Structurer:
    def __init__(
        self,
        content: str,
        color: Optional[str] = None,
        highlight: Optional[str] = None,
        style: Optional[str] = None,
    ):
        self.content = content
        self.color = color if color else ""
        self.highlight = highlight if highlight else ""
        self.style = list(map(str.strip, style.split(","))) if style else ""
        self.painted_content = self.content

    def form(self) -> Form:
        return {
            "content": self.content,
            "color": self.color,
            "highlight": self.highlight,
            "style": self.style,
            "painted_content": self.content,
            "styled_content": self.content,
        }
