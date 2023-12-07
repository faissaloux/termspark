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

    def reformat(
        self, content: Dict[str, list], detected: Dict[int, list]
    ) -> List[str]:
        for index in range(len(content["content"])):
            new_content = content["content"].copy()
            step = index

            # Isolate hyperlinks from texts.
            if index in detected:
                for hyperlink_index in range(len(detected[index]) - 1, -1, -1):
                    hyperlink = detected[index][hyperlink_index]
                    hyperlink_markdown = f"[{hyperlink[0]}]({hyperlink[1]})"
                    hyperlink_position = new_content[index].rfind(hyperlink_markdown)

                    new_content.insert(
                        index + 1, new_content[index][hyperlink_position:]
                    )
                    new_content[index] = new_content[index].replace(
                        new_content[index][hyperlink_position:], ""
                    )

                    content["color"].insert(index + 1, content["color"][index])
                    content["highlight"].insert(index + 1, content["highlight"][index])
                    content["style"].insert(index + 1, content["style"][index])

                    self.__hyperlink_elements.append(step + 1)
                    step += 1

            content["content"] = new_content

        for index, element in enumerate(new_content):
            matches = re.findall(self.HYPERLINK_PATTERN, element)
            if len(matches):
                self.matches.append(matches)
            else:
                self.matches.append([])

        return content["content"]

    @staticmethod
    def exists_in(content: List[str]) -> Dict[int, list]:
        detected: Dict[int, list] = {}

        for index, element in enumerate(content):
            if hyperlink := re.findall(Hyperlink.HYPERLINK_PATTERN, element):
                detected[index] = hyperlink

        return detected

    def encode(self) -> List[Union[str, List[Dict[str, str]]]]:
        encoded: List[Union[str, List[Dict[str, str]]]] = []

        for index in range(len(self.content)):
            if index in self.__hyperlink_elements:
                encoded.append(self.__encode_single(index))
            else:
                encoded.append([])

        return encoded

    def __encode_single(self, content_index: int) -> List[Dict[str, str]]:
        encoded_hyperlinks: List[Dict[str, str]] = []

        for match in self.matches[content_index]:
            encoded_hyperlink: str = (
                self.HYPERLINK_PREFIX
                + match[1]
                + self.RESET
                + match[0]
                + self.HYPERLINK_SUFFIX
                + self.RESET
            )

            encoded_hyperlinks.append(
                {
                    match[0]: re.sub(
                        self.HYPERLINK_PATTERN,
                        encoded_hyperlink,
                        f"[{match[0]}]({match[1]})",
                        1,
                    )
                }
            )

        return encoded_hyperlinks
