import os
from itertools import chain
from typing import Dict, List, Optional

from .exceptions.combinationException import CombinationException
from .exceptions.emptyException import EmptyException
from .exceptions.lenNotSupportedException import LenNotSupportedException
from .exceptions.minNotReachedException import MinNotReachedException
from .exceptions.multiplePositionsNotSupported import MultiplePositionsNotSupported
from .helpers.existenceChecker import ExistenceChecker
from .painter.painter import Painter
from .structurer.structurer import Structurer
from .validators.printerValidator import PrinterValidator


class TermSpark:
    __silent: List[str] = []

    mode: str = "color"
    width: int = 0
    left: Dict[str, str] = {}
    right: Dict[str, str] = {}
    center: Dict[str, str] = {}
    separator: Dict[str, str] = {
        "content": " ",
        "color": "",
        "highlight": "",
        "painted_content": " ",
    }
    separator_is_set: bool = False
    line_is_set: bool = False
    is_full_width: bool = False
    colors: chain = chain(range(30, 37), range(90, 97))
    highlights: chain = chain(range(41, 47), range(100, 108))
    attributes: range = range(1, 9)
    design_codes: List[str] = []
    positions: List[str] = [
        "left",
        "center",
        "right",
    ]

    def __init__(self):
        self.__set_design_codes()

    def print_left(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        PrinterValidator().validate(content, color, highlight)

        self.spark_left([content, color, highlight])  # type: ignore

        return self

    def print_right(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        PrinterValidator().validate(content, color, highlight)

        self.spark_right([content, color, highlight])  # type: ignore

        return self

    def print_center(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        PrinterValidator().validate(content, color, highlight)

        self.spark_center([content, color, highlight])  # type: ignore

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
        self, positionContent: Dict[str, List[str]], *content: str
    ):
        if not positionContent:
            positionContent["content"] = [Structurer(*content).form()["content"]]
            positionContent["color"] = [Structurer(*content).form()["color"]]
            positionContent["highlight"] = [Structurer(*content).form()["highlight"]]
        else:
            positionContent["content"].append(Structurer(*content).form()["content"])
            positionContent["color"].append(Structurer(*content).form()["color"])
            positionContent["highlight"].append(
                Structurer(*content).form()["highlight"]
            )

        return positionContent

    def set_separator(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        if len(content) != 1:
            raise LenNotSupportedException("separator", 1)

        self.separator = Structurer(content, color, highlight).form()

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
        colors_codes_length = self.calculate_colors_codes_length()
        content_length = 0

        for position in self.positions:
            painted_content = ExistenceChecker().dictionary_key(
                getattr(self, position), "painted_content"
            )
            content_length += len(painted_content)
        self.separator["length"] = (
            self.get_width() - content_length + colors_codes_length
        )

    def calculate_colors_codes_length(self) -> int:
        colors_codes_length = 0

        for design_code in self.design_codes:
            for position in self.positions:
                position_content = ExistenceChecker().dictionary_key(
                    getattr(self, position), "painted_content"
                )
                if design_code in position_content:
                    colors_codes_length += (
                        len(design_code) * position_content.count(design_code)
                    ) + position_content.count(design_code)

        return colors_codes_length - len("\x1b")

    def line(self, separator: Optional[str] = None, highlight: Optional[str] = None):
        self.__silent.append("separator")
        self.set_separator(
            separator if separator else self.separator["content"], highlight=highlight
        )

        self.line_is_set = True

        return self

    def __set_design_codes(self):
        for color in self.colors:
            if f"[{color}m" not in self.design_codes:
                self.design_codes.append(f"[{color}m")
        for highlight in self.highlights:
            if f"[{highlight}m" not in self.design_codes:
                self.design_codes.append(f"[{highlight}m")
        for attribute in self.attributes:
            if f"[{attribute}m" not in self.design_codes:
                self.design_codes.append(f"[{attribute}m")

        if f"[0m" not in self.design_codes:
            self.design_codes.append("[0m")

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

    def render(self) -> str:
        self.__paint_content()
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
            self.separator["painted_content"] * half_separator_length
        )

        center_content = ExistenceChecker().dictionary_key(self.center, "content")
        if len(center_content) > 0:
            if self.mode == "raw":
                center = (
                    separator_mid_width + self.center["content"]
                    if isinstance(self.center["content"], str)
                    else " ".join(center_content) + separator_mid_width
                )
            else:
                center = (
                    separator_painted_mid_width
                    + self.center["painted_content"]
                    + separator_painted_mid_width
                )
        else:
            center = self.separator["painted_content"] * int(self.separator["length"])

        if self.mode == "raw":
            left_content = ExistenceChecker().dictionary_key(self.left, "content")
            right_content = ExistenceChecker().dictionary_key(self.right, "content")

            if len(left_content) > 0:
                left_content = (
                    self.left["content"]
                    if isinstance(self.left["content"], str)
                    else " ".join(left_content)
                )

            if len(right_content) > 0:
                right_content = (
                    self.right["content"]
                    if isinstance(self.right["content"], str)
                    else " ".join(right_content)
                )
        else:
            left_content = ExistenceChecker().dictionary_key(
                self.left, "painted_content"
            )
            right_content = ExistenceChecker().dictionary_key(
                self.right, "painted_content"
            )

        return left_content + center + right_content

    def __paint_content(self):
        for position in self.positions:
            pos = getattr(self, position) if getattr(self, position) else {}
            if pos:
                pos["painted_content"] = Painter().element(pos).paint()

            setattr(self, position, pos)

    def __paint_separator(self):
        if "color" in self.separator or "highlight" in self.separator:
            self.separator["painted_content"] = (
                Painter().element(self.separator).paint()
            )

    def __trim(self, chars_number):
        self.positions.reverse()
        chars_number_left = chars_number

        for position in self.positions:
            new_content = []
            if "content" in getattr(self, position).keys():
                getattr(self, position)["content"].reverse()
                for content in getattr(self, position)["content"]:
                    if chars_number_left > 0:
                        if len(content) > chars_number_left:
                            new_content.append(
                                content[0 : len(content) - chars_number_left - 1]
                            )
                            chars_number_left -= chars_number
                        else:
                            chars_number_left = chars_number_left - len(content)
                    else:
                        new_content.append(content)

                getattr(self, position)["content"] = new_content
                getattr(self, position)["content"].reverse()

        self.positions.reverse()
        self.mode = "color"

        print(self.render())

    def spark(self, end="\n"):
        raw = self.raw()
        to_trim = len(raw) - self.get_terminal_width() - 1

        if to_trim > 0:
            self.__trim(to_trim)
        else:
            self.mode = "color"
            if self.is_full_width:
                self.__take_full_width()
            print(self.render(), end=end)

    def raw(self) -> str:
        self.mode = "raw"
        return self.render()

    def __repr__(self) -> str:
        return self.render()
