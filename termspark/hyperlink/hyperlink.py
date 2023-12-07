import re
from typing import Dict, List, Union


class Hyperlink:
    PLACEHOLDER_PATTERN: str = "[^\\[]*?"
    URL_PATTERN: str = "http[s]?://[^)]+"
    HYPERLINK_PATTERN: str = f"\\[({PLACEHOLDER_PATTERN})]\\(\\s*({URL_PATTERN})\\s*\\)"

    HYPERLINK_PREFIX: str = "\x1b]8;;"
    HYPERLINK_SUFFIX: str = "\x1b]8;;"
    RESET: str = "\x1b\\\\"

    matches: list = []

    def __init__(self):
        self.__hyperlink_elements: list = []

    def set_content(self, content: List[str]):
        self.content = content

    def exists(self) -> bool:
        self.matches = []
        matches_length: int = 0

        for index, content in enumerate(self.content):
            matches = re.findall(Hyperlink.HYPERLINK_PATTERN, content)
            if len(matches):
                self.content[index] = ""
                for match in matches:
                    self.content[index] += f"[{match[0]}]({match[1]})"

                self.matches.append(matches)
            else:
                self.matches.append([])

        for index, match in enumerate(self.matches):
            if len(match):
                matches_length += 1
                self.__hyperlink_elements.append(index)

        return matches_length > 0

    def encode(self) -> List[Union[str, List[Dict[str, str]]]]:
        encoded: List[Union[str, List[Dict[str, str]]]] = []

        for index, content in enumerate(self.content):
            if index in self.__hyperlink_elements:
                encoded.append(self.__encode_single(index))
            else:
                encoded.append(content)

        return encoded

    def __encode_single(self, content_index: int) -> List[Dict[str, str]]:
        encoded_hyperlinks: List[Dict[str, str]] = []

        for match in self.matches[content_index]:
            encoded_hyperlink: str = (
                Hyperlink.HYPERLINK_PREFIX
                + match[1]
                + Hyperlink.RESET
                + match[0]
                + Hyperlink.HYPERLINK_SUFFIX
                + Hyperlink.RESET
            )

            encoded_hyperlinks.append(
                {
                    match[0]: re.sub(
                        Hyperlink.HYPERLINK_PATTERN,
                        encoded_hyperlink,
                        f"[{match[0]}]({match[1]})",
                        1,
                    )
                }
            )

        return encoded_hyperlinks
