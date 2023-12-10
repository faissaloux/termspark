import re
from typing import Dict, Final, List, TypedDict

EncodedHyperlink = TypedDict(
    "EncodedHyperlink",
    {
        "index": int,
        "placeholder": str,
        "hyperlink": str,
    },
    total=False,
)

HyperlinkMatch = TypedDict(
    "HyperlinkMatch",
    {
        "index": int,
        "placeholder": str,
        "link": str,
    },
    total=False,
)


class Hyperlink:
    PLACEHOLDER_PATTERN: Final[str] = "[^\\[]*?"
    URL_PATTERN: Final[str] = "http[s]?://[^)]+"
    HYPERLINK_PATTERN: Final[
        str
    ] = f"\\[({PLACEHOLDER_PATTERN})]\\(\\s*({URL_PATTERN})\\s*\\)"

    HYPERLINK_PREFIX: Final[str] = "\x1b]8;;"
    HYPERLINK_SUFFIX: Final[str] = "\x1b]8;;"
    RESET: Final[str] = "\x1b\\\\"

    def __init__(self):
        self.__hyperlinks_positions: list = []
        self.matches: List[HyperlinkMatch] = []

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

                            self.__copy_attributes(content, index, 1)

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
                                self.__copy_attributes(content, index, 1)

                                # Update hyperlinks positions.
                                for idx, elem in enumerate(self.__hyperlinks_positions):
                                    self.__hyperlinks_positions[idx] = (
                                        elem + 1 if elem > i else elem
                                    )

            content["content"] = new_content

        for index, element in enumerate(new_content):
            matches = re.findall(self.HYPERLINK_PATTERN, element)
            if len(matches):
                match = matches[0]
                self.matches.append(
                    {
                        "index": index,
                        "placeholder": match[0],
                        "link": match[1],
                    }
                )

        return content["content"]

    @staticmethod
    def exists_in(content: List[str]) -> Dict[int, list]:
        detected: Dict[int, list] = {}

        for index, element in enumerate(content):
            if hyperlink := re.findall(Hyperlink.HYPERLINK_PATTERN, element):
                detected[index] = hyperlink

        return detected

    def __copy_attributes(
        self,
        content: Dict[str, list],
        index: int,
        step: int,
        attributes: List[str] = ["color", "highlight", "style"],
    ) -> None:
        for attribute in attributes:
            content[attribute].insert(index + step, content[attribute][index])

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

    def encode(self) -> List[EncodedHyperlink]:
        encoded: List[EncodedHyperlink] = []

        for index in range(len(self.content)):
            if index in self.__hyperlinks_positions:
                encoded.append(self.__encode_single(index))

        return encoded

    def __encode_single(self, content_index: int) -> EncodedHyperlink:
        match: HyperlinkMatch = list(
            filter(lambda match: match["index"] == content_index, self.matches)
        )[0]
        placeholder: str = match["placeholder"]
        link: str = match["link"]

        encoded_hyperlink: str = (
            self.HYPERLINK_PREFIX
            + link
            + self.RESET
            + placeholder
            + self.HYPERLINK_SUFFIX
            + self.RESET
        )

        return {
            "index": content_index,
            "placeholder": placeholder,
            "hyperlink": re.sub(
                self.HYPERLINK_PATTERN,
                encoded_hyperlink,
                f"[{placeholder}]({link})",
                1,
            ),
        }
