from typing import Optional, Sequence, Union

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
        self.content: str = content
        self.color: str = color if color else ""
        self.highlight: str = highlight if highlight else ""
        self.style: Union[str, Sequence[str]] = (
            list(map(str.strip, style.split(","))) if style else ""
        )
        self.painted_content: str = self.content

    def form(self) -> Form:
        return {
            "content": self.content,
            "color": self.color,
            "highlight": self.highlight,
            "style": self.style,
            "painted_content": self.content,
            "styled_content": self.content,
        }
