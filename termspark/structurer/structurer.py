from typing import Final, Optional, Sequence, Union

from typing_extensions import TypedDict

Form = TypedDict(
    "Form",
    {
        "content": str,
        "color": str,
        "highlight": str,
        "style": Sequence[str],
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
        self.content: Final[str] = content
        self.color: Final[str] = color if color else ""
        self.highlight: Final[str] = highlight if highlight else ""
        self.style: Union[str, Sequence[str]] = (
            list(map(str.strip, style.split(","))) if style else ""
        )

    def form(self) -> Form:
        return {
            "content": str(self.content),
            "color": self.color,
            "highlight": self.highlight,
            "style": self.style,
            "styled_content": self.content,
        }
