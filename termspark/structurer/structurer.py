from typing import Dict, Optional


class Structurer:
    def __init__(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        self.content = content
        self.color = color
        self.highlight = highlight

    def form(self) -> Dict[str, str]:
        return {
            "content": self.content if self.content else "",
            "color": self.color if self.color else "",
            "highlight": self.highlight if self.highlight else "",
        }
