import re
from typing import Dict, List, Union


class Hyperlink:
    PLACEHOLDER_PATTERN: str = "[^\\[]*?"
    URL_PATTERN: str = "http[s]?://[^)]+"
    HYPERLINK_PATTERN: str = f"\\[({PLACEHOLDER_PATTERN})]\\(\\s*({URL_PATTERN})\\s*\\)"

    HYPERLINK_PREFIX: str = "\x1b]8;;"
    HYPERLINK_SUFFIX: str = "\x1b]8;;"
    RESET: str = "\x1b\\\\"

    def __init__(self):
        self.__hyperlinks_positions: list = []
        self.matches: list = []

    def set_content(self, content: List[str]):
        self.content = content

    def reformat(
        self, content: Dict[str, list], detected: Dict[int, list]
    ) -> List[str]:
        for index in range(len(content["content"]) - 1, -1, -1):
            new_content = content["content"].copy()

            # Isolate hyperlinks from texts.
            if index in detected:
                for hyperlink_index in range(len(detected[index]) - 1, -1, -1):
                    hyperlink = detected[index][hyperlink_index]
                    hyperlink_markdown = f"[{hyperlink[0]}]({hyperlink[1]})"
                    hyperlink_position = new_content[index].rfind(hyperlink_markdown)

                    if hyperlink_position >= 0:
                        hyperlink_to_insert = new_content[index][hyperlink_position:]
                        if new_content[index] != hyperlink_to_insert:
                            new_content.insert(index + 1, hyperlink_to_insert)
                            new_content[index] = new_content[index].replace(
                                hyperlink_to_insert, ""
                            )

                            content["color"].insert(index + 1, content["color"][index])
                            content["highlight"].insert(
                                index + 1, content["highlight"][index]
                            )
                            content["style"].insert(index + 1, content["style"][index])

                            self.__hyperlinks_positions = [
                                elem + 1 for elem in self.__hyperlinks_positions
                            ]
                            self.__hyperlinks_positions.append(index + 1)
                        else:
                            self.__hyperlinks_positions.append(index)

                        # Isolate hyperlink from extra whitespace.
                        for i, element in enumerate(new_content):
                            if element == hyperlink_to_insert and " " in element:
                                extra_white_space = " " * element.count(" ")
                                new_content[i] = element.rstrip()

                                new_content.insert(i + 1, extra_white_space)
                                content["color"].insert(
                                    index + 1, content["color"][index]
                                )
                                content["highlight"].insert(
                                    index + 1, content["highlight"][index]
                                )
                                content["style"].insert(
                                    index + 1, content["style"][index]
                                )

                                # Update hyperlinks positions.
                                for idx, elem in enumerate(self.__hyperlinks_positions):
                                    if elem > i:
                                        self.__hyperlinks_positions[idx] = elem + 1
                                    else:
                                        self.__hyperlinks_positions[idx] = elem

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

    def placeholders(self) -> List[str]:
        """Replaces hyperlinks in content with their placeholders."""

        replaces: Dict[str, str] = {}
        updated_content: List[str] = []

        for content in self.content:
            replaced_content: str = content
            hyperlinks_found = re.findall(Hyperlink.HYPERLINK_PATTERN, content)

            for hyperlink_found in hyperlinks_found:
                replaces[
                    f"[{hyperlink_found[0]}]({hyperlink_found[1]})"
                ] = hyperlink_found[0]

            for replace_from, replace_by in replaces.items():
                replaced_content = replaced_content.replace(replace_from, replace_by)

            updated_content.append(replaced_content)

        return updated_content

    def encode(self) -> List[Union[str, List[Dict[str, str]]]]:
        encoded: List[Union[str, List[Dict[str, str]]]] = []

        for index in range(len(self.content)):
            if index in self.__hyperlinks_positions:
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
