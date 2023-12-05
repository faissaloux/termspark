import os
import re
from typing import Dict, List, Optional, Sequence, Union

from typing_extensions import TypedDict

from .exceptions.combinationException import CombinationException
from .exceptions.emptyException import EmptyException
from .exceptions.lenNotSupportedException import LenNotSupportedException
from .exceptions.minNotReachedException import MinNotReachedException
from .exceptions.multiplePositionsNotSupported import MultiplePositionsNotSupported
from .helpers.existenceChecker import ExistenceChecker
from .hyperlink.hyperlink import Hyperlink
from .structurer.structurer import Structurer
from .styler.styler import Styler
from .validators.printerValidator import PrinterValidator

Separator = TypedDict(
    "Separator",
    {
        "content": List[str],
        "color": List[str],
        "highlight": List[str],
        "painted_content": List[str],
        "style": List[Union[str, Sequence[str]]],
        "styled_content": List[str],
        "length": int,
    },
    total=False,
)


class TermSpark:
    __silent: List[str] = []

    mode: str = "color"
    width: int = 0
    hyperlink_trash_length: int = 0
    left: Dict[str, str] = {}
    right: Dict[str, str] = {}
    center: Dict[str, str] = {}
    separator: Separator = {}
    separator_is_set: bool = False
    line_is_set: bool = False
    is_full_width: bool = False
    to_trim: dict[str, dict[int, str]] = {}
    positions: List[str] = [
        "left",
        "center",
        "right",
    ]

    def __init__(self):
        self.__silent.append("separator")
        self.set_separator(" ")

    def print_left(
        self,
        content: str,
        color: Optional[str] = None,
        highlight: Optional[str] = None,
        style: Optional[str] = None,
    ):
        PrinterValidator("left").validate(content, color, highlight, style)

        self.spark_left([content, color, highlight, style])  # type: ignore

        return self

    def print_right(
        self,
        content: str,
        color: Optional[str] = None,
        highlight: Optional[str] = None,
        style: Optional[str] = None,
    ):
        PrinterValidator("right").validate(content, color, highlight, style)

        self.spark_right([content, color, highlight, style])  # type: ignore

        return self

    def print_center(
        self,
        content: str,
        color: Optional[str] = None,
        highlight: Optional[str] = None,
        style: Optional[str] = None,
    ):
        PrinterValidator("center").validate(content, color, highlight, style)

        self.spark_center([content, color, highlight, style])  # type: ignore

        return self

    def spark_left(self, *contents: List[str]):
        self.__spark_position("left", *contents)

        return self

    def spark_right(self, *contents: List[str]):
        self.__spark_position("right", *contents)

        return self

    def spark_center(self, *contents: List[str]):
        self.__spark_position("center", *contents)

        return self

    def __spark_position(self, position: str, *contents: List[str]):
        positionContent = getattr(self, position) if getattr(self, position) else {}

        if not isinstance(contents[0], list):
            contents = (list(contents),)

        for content in contents:
            positionContent = self.__appendPositionContent(positionContent, *content)

        setattr(self, position, positionContent)

    def __max_position(self, position: str, max: int):
        if max < 1:
            raise MinNotReachedException("max", 1)

        chars_number = max
        new_content = []
        breakIndex = 0

        for index, sentence in enumerate(getattr(self, position)["content"]):
            if chars_number <= 0:
                break

            if len(sentence) < chars_number:
                new_content.append(sentence)
                chars_number -= len(sentence)
            elif len(sentence) == chars_number:
                new_content.append(sentence[0:chars_number])
                chars_number -= len(sentence)
                breakIndex = index + 1
            else:
                new_content.append(sentence[0:chars_number])
                chars_number -= len(sentence)
                breakIndex = index + 1

        getattr(self, position)["content"] = new_content
        getattr(self, position)["color"] = getattr(self, position)["color"][
            0:breakIndex
        ]
        getattr(self, position)["highlight"] = getattr(self, position)["highlight"][
            0:breakIndex
        ]

    def max_left(self, max: int):
        self.__max_position("left", max)

        return self

    def max_right(self, max: int):
        self.__max_position("right", max)

        return self

    def max_center(self, max: int):
        self.__max_position("center", max)

        return self

    def __appendPositionContent(
        self, positionContent: Dict[str, List[Union[str, Sequence[str]]]], *content: str
    ):
        if not positionContent:
            positionContent["content"] = [Structurer(*content).form()["content"]]
            positionContent["color"] = [Structurer(*content).form()["color"]]
            positionContent["highlight"] = [Structurer(*content).form()["highlight"]]
            positionContent["style"] = [Structurer(*content).form()["style"]]
        else:
            positionContent["content"].append(Structurer(*content).form()["content"])
            positionContent["color"].append(Structurer(*content).form()["color"])
            positionContent["highlight"].append(
                Structurer(*content).form()["highlight"]
            )
            positionContent["style"].append(Structurer(*content).form()["style"])

        return positionContent

    def set_separator(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        if len(content) != 1:
            raise LenNotSupportedException("separator", 1)

        self.separator["content"] = [
            Structurer(content, color, highlight).form()["content"]
        ]
        self.separator["color"] = [
            Structurer(content, color, highlight).form()["color"]
        ]
        self.separator["highlight"] = [
            Structurer(content, color, highlight).form()["highlight"]
        ]
        self.separator["painted_content"] = [
            Structurer(content, color, highlight).form()["painted_content"]
        ]
        self.separator["style"] = [
            Structurer(content, color, highlight).form()["style"]
        ]
        self.separator["styled_content"] = [
            Structurer(content, color, highlight).form()["styled_content"]
        ]

        if "separator" not in self.__silent:
            self.separator_is_set = True
        else:
            self.__silent.remove("separator")

        return self

    def set_width(self, width: int):
        self.width = width

        return self

    def full_width(self):
        self.is_full_width = True

        return self

    def __calculate_separator_length(self):
        content_length = 0

        for position in self.positions:
            content = ExistenceChecker().dictionary_key(
                getattr(self, position), "content"
            )

            content_length += len("".join(content))

        self.separator["length"] = self.get_width() - content_length

    def line(self, separator: Optional[str] = None, highlight: Optional[str] = None):
        self.__silent.append("separator")

        self.set_separator(
            separator if separator else self.separator["content"][0],
            highlight=highlight,
        )

        self.line_is_set = True

        return self

    def get_terminal_width(self) -> int:
        try:
            width = os.get_terminal_size()[0]
        except OSError:
            width = 80

        return width

    def get_width(self) -> int:
        if self.width == 0:
            self.width = self.get_terminal_width()

        return self.width

    def __take_full_width(self):
        not_empty_positions = 0
        active_position = None

        for position in self.positions:
            if "content" in getattr(self, position):
                active_position = position
                not_empty_positions += 1

        if not_empty_positions > 1:
            raise MultiplePositionsNotSupported()

        empty_space = self.get_width() - len(
            "".join(getattr(self, active_position)["content"])
        )

        if active_position == "left":
            extra_left_space = ""
            extra_right_space = " " * empty_space
        elif active_position == "right":
            extra_left_space = " " * empty_space
            extra_right_space = ""
        else:
            half_empty_space = empty_space // 2

            extra_left_space = " " * half_empty_space
            extra_right_space = (
                " " * (half_empty_space + 1)
                if empty_space % 2 != 0
                else " " * half_empty_space
            )

        getattr(self, active_position)["content"][0] = (
            extra_left_space + getattr(self, active_position)["content"][0]
        )

        getattr(self, active_position)["content"][-1] = (
            getattr(self, active_position)["content"][-1] + extra_right_space
        )

        getattr(self, active_position)["encoded_content"] = getattr(
            self, active_position
        )["content"]

    def render(self) -> str:
        if self.mode == "color":
            self.__style_content()
        self.__calculate_separator_length()
        if self.mode == "color":
            self.__paint_separator()

        if self.line_is_set and self.separator_is_set:
            raise CombinationException("line", "separator")

        if (
            not any(
                [
                    "content" in self.left,
                    "content" in self.right,
                    "content" in self.center,
                ]
            )
            and not self.line_is_set
        ):
            raise EmptyException

        half_separator_length = int(self.separator["length"]) // 2
        separator_mid_width = self.separator["content"] * half_separator_length
        separator_painted_mid_width = (
            self.separator["styled_content"][0] * half_separator_length
        )

        center_content = ExistenceChecker().dictionary_key(self.center, "content")

        # trim what should be trimmed
        if self.mode != "raw" and len(self.to_trim):
            for position in self.positions:
                if position in self.to_trim and len(self.to_trim[position]):
                    text_to_trim = "".join(self.to_trim[position].values())
                    styled_content = getattr(self, position)["styled_content"]
                    getattr(self, position)["styled_content"] = "".join(
                        styled_content.rsplit(text_to_trim, 1)
                    )

        if len(center_content) > 0:
            if self.mode == "raw":
                center = " ".join(center_content) + "".join(separator_mid_width)
            else:
                center = (
                    separator_painted_mid_width
                    + self.center["styled_content"]
                    + separator_painted_mid_width
                )
        else:
            center = self.separator["styled_content"][0] * int(self.separator["length"])
            center = "".join(center)

        if self.mode == "raw":
            left_content = ExistenceChecker().dictionary_key(self.left, "content")
            right_content = ExistenceChecker().dictionary_key(self.right, "content")

            if len(left_content) > 0:
                left_content = " ".join(left_content)

            if len(right_content) > 0:
                right_content = " ".join(right_content)
        else:
            left_content = ExistenceChecker().dictionary_key(
                self.left, "styled_content"
            )
            right_content = ExistenceChecker().dictionary_key(
                self.right, "styled_content"
            )

        return left_content + center + right_content

    def __style_content(self):
        for position in self.positions:
            pos = getattr(self, position) if getattr(self, position) else {}

            if pos:
                pos["styled_content"] = Styler().element(pos).style()

            setattr(self, position, pos)

    def __paint_separator(self):
        self.separator["styled_content"] = [Styler().element(self.separator).style()]

    def __trim(self, chars_number):
        chars_number_left = chars_number

        for posIndex in range(len(self.positions) - 1, -1, -1):
            position = self.positions[posIndex]
            if "content" in getattr(self, position).keys():
                self.to_trim[position] = {}
                position_content = getattr(self, position)["content"]
                for content_index in range(len(position_content) - 1, -1, -1):
                    content = position_content[content_index]
                    if chars_number_left > 0:
                        if len(content) > chars_number_left:
                            self.to_trim[position][content_index] = content[
                                len(content) - chars_number_left :
                            ]
                            chars_number_left -= chars_number
                        else:
                            self.to_trim[position][content_index] = content
                            chars_number_left = chars_number_left - len(content)

    def spark(self, end="\n"):
        for position in self.positions:
            pos = getattr(self, position)
            positionContent = pos
            if "content" in pos:
                hyperlink = Hyperlink()
                hyperlink.set_content(pos["content"].copy())
                if hyperlink.exists():
                    positionContent["hyperlinks"] = hyperlink.encode()
                    replaces: Dict[str, str] = {}
                    updated_content: List[str] = []
                    for content in pos["content"]:
                        replaced_content: List[str] = content
                        hyperlinks_found = re.findall(
                            Hyperlink.HYPERLINK_PATTERN, content
                        )
                        for hyperlink in hyperlinks_found:
                            replaces[f"[{hyperlink[0]}]({hyperlink[1]})"] = hyperlink[0]

                        for replace_from, replace_by in replaces.items():
                            replaced_content = replaced_content.replace(
                                replace_from, replace_by
                            )

                        updated_content.append(replaced_content)
                    positionContent["content"] = updated_content

            setattr(self, position, positionContent)

        raw = self.raw()
        to_trim = len(raw) - self.get_terminal_width() - 1
        if to_trim > 0:
            self.__trim(to_trim)
        else:
            if self.is_full_width:
                self.__take_full_width()

        # Apply hyperlinks
        for position in self.positions:
            pos = getattr(self, position)
            if "hyperlinks" in pos:
                pos["encoded_content"] = pos["content"].copy()
                for index, hyperlinks in enumerate(pos["hyperlinks"]):
                    if isinstance(hyperlinks, dict):
                        for placeholder, hyperlink in hyperlinks.items():
                            pos["encoded_content"][index] = pos["encoded_content"][
                                index
                            ].replace(placeholder, hyperlink.strip())

        self.mode = "color"
        print(self.render(), end=end)

    def raw(self) -> str:
        self.mode = "raw"
        return self.render()

    def __repr__(self) -> str:
        return self.render()
