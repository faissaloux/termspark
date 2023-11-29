from typing import Dict, Optional


class Structurer:
    def __init__(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        self.content = content
        self.color = color if color else ""
        self.highlight = highlight if highlight else ""
        self.painted_content = self.content

    def form(self) -> Dict[str, str]:
        return {
            "content": self.content,
            "color": self.color,
            "highlight": self.highlight,
            "painted_content": self.content,
        }
