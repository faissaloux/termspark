import re


class Hyperlink:
    PLACEHOLDER_PATTERN: str = "[^]]+"
    URL_PATTERN: str = "http[s]?://[^)]+"
    HYPERLINK_PATTERN: str = f"\\[({PLACEHOLDER_PATTERN})]\\(\\s*({URL_PATTERN})\\s*\\)"

    URL_PREFIX: str = "\x1b]8;;"
    PLACEHOLDER_SUFFIX: str = "\x1b]8;;"
    RESET: str = "\x1b;"

    trash: str = ""

    def set_content(self, content: str):
        self.content = content

    def exists(self) -> bool:
        matches = re.findall(Hyperlink.HYPERLINK_PATTERN, self.content)

        self.matches = matches[0] if len(matches) else []

        return len(self.matches) > 1

    def encode(self) -> str:
        encoded_hyperlink: str = (
            Hyperlink.URL_PREFIX
            + self.matches[1]
            + Hyperlink.RESET
            + self.matches[0]
            + Hyperlink.PLACEHOLDER_SUFFIX
            + Hyperlink.RESET * 2
        )

        self.trash += self.matches[1]
        self.trash += (
            Hyperlink.URL_PREFIX + Hyperlink.RESET * 3 + Hyperlink.PLACEHOLDER_SUFFIX
        )

        return re.sub(Hyperlink.HYPERLINK_PATTERN, encoded_hyperlink, self.content)

    def trash_length(self) -> int:
        return len(self.trash)
