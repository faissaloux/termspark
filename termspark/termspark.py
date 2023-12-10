import os
from typing import Dict, Final, List, Optional, Sequence, Union

from termspark.line.line import Line

from .exceptions.combination_error import CombinationError
from .exceptions.empty_error import EmptyError
from .exceptions.len_not_supported_error import LenNotSupportedError
from .exceptions.min_not_reached_error import MinNotReachedError
from .exceptions.multiple_positions_not_supported_error import (
    MultiplePositionsNotSupportedError,
)
from .hyperlink.hyperlink import EncodedHyperlink, Hyperlink
from .separator.separator import Separator
from .structurer.structurer import Structurer
from .styler.styler import Styler
from .trimer.trimer import Trimer
from .validators.printer_validator import PrinterValidator


class TermSpark:
    POSITIONS: Final[List[str]] = [
        "left",
        "center",
        "right",
    ]

    mode: str = "color"
    width: int = 0
    left: Dict[str, str] = {}
    right: Dict[str, str] = {}
    center: Dict[str, str] = {}
    is_full_width: bool = False
    to_trim: Dict[str, Dict[int, str]] = {}

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
            raise MinNotReachedError("max", 1)

        chars_number = max
        new_content = []
        breakIndex = 0

        for index, sentence in enumerate(getattr(self, position)["content"]):
            if chars_number <= 0:
                break

            if len(sentence) < chars_number:
                new_content.append(sentence)
            else:
                new_content.append(sentence[0:chars_number])
                breakIndex = index + 1

            chars_number -= len(sentence)

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
        structured_data = Structurer(*content).form()

        if not positionContent:
            positionContent = {
                key: [] for key in ["content", "color", "highlight", "style"]
            }

        for elem in positionContent:
            positionContent[elem].append(
                structured_data[elem]  # type:ignore[literal-required]
            )

        return positionContent

    def set_separator(
        self, content: str, color: Optional[str] = None, highlight: Optional[str] = None
    ):
        if len(content) != 1:
            raise LenNotSupportedError("separator", 1)

        structured_data = Structurer(content, color, highlight).form()
        self.separator = Separator(structured_data)

        return self

    def line(self, pattern: Optional[str] = None, highlight: Optional[str] = None):
        pattern = pattern if pattern else " "

        structured_data = Structurer(pattern, highlight=highlight).form()
        self.line_separator = Line(structured_data)

        return self

    def set_width(self, width: int):
        self.width = width

        return self

    def full_width(self):
        self.is_full_width = True

        return self

    def __calculate_separator_length(self):
        content_length = 0

        for position in self.POSITIONS:
            content = getattr(self, position).get("content", "")

            content_length += len("".join(content))

        self.separator.set_length(self.get_width() - content_length)

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

        for position in self.POSITIONS:
            if "content" in getattr(self, position):
                active_position = position
                not_empty_positions += 1

        if not_empty_positions > 1:
            raise MultiplePositionsNotSupportedError()

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
        if hasattr(self, "separator") and hasattr(self, "line_separator"):
            raise CombinationError("line", "separator")

        if not any(
            [
                "content" in self.left,
                "content" in self.right,
                "content" in self.center,
            ]
        ) and not hasattr(self, "line_separator"):
            raise EmptyError

        if hasattr(self, "line_separator"):
            if self.mode == "raw":
                return self.line_separator.get_raw_content()["full"] * self.get_width()

            self.line_separator.style()

            return self.line_separator.get_styled_content()["full"] * self.get_width()

        if not hasattr(self, "separator"):
            self.set_separator(" ")

        if self.mode == "color":
            self.__style_content()
            self.separator.style()

        self.__calculate_separator_length()

        # Trim what should be trimmed.
        if self.mode != "raw" and hasattr(self, "trimer"):
            self.__trim()

        styled_separator = self.separator.get_styled_content()
        center_content = self.center.get("content", "")

        if len(center_content) > 0:
            if self.mode == "raw":
                raw_separator = self.separator.get_raw_content()
                center = (
                    raw_separator["left"]
                    + "".join(center_content)
                    + raw_separator["right"]
                )
            else:
                center = (
                    styled_separator["left"]
                    + "".join(self.center["styled_content"])
                    + styled_separator["right"]
                )
        else:
            center = styled_separator["full"]

        content_type = "content" if self.mode == "raw" else "styled_content"

        left_content = self.left.get(content_type, "")
        right_content = self.right.get(content_type, "")

        return "".join(left_content) + center + "".join(right_content)

    def __style_content(self):
        for position in self.POSITIONS:
            pos = getattr(self, position) if getattr(self, position) else {}

            if pos:
                pos["styled_content"] = Styler().element(pos).style()

            setattr(self, position, pos)

    def __detect_hyperlinks(self) -> None:
        for position in self.POSITIONS:
            positionContent = getattr(self, position)

            if "content" in positionContent:
                detected = Hyperlink.exists_in(positionContent["content"])
                if detected:
                    hyperlink = Hyperlink()
                    reformated = hyperlink.reformat(positionContent, detected)
                    hyperlink.set_content(reformated)
                    positionContent["hyperlinks"] = hyperlink.encode()
                    positionContent["content"] = hyperlink.placeholders()

            setattr(self, position, positionContent)

    def __apply_hyperlinks(self) -> None:
        for position in self.POSITIONS:
            pos = getattr(self, position)
            if "hyperlinks" in pos:
                pos["encoded_content"] = self.__apply_hyperlinks_to_content(
                    pos["content"], pos["hyperlinks"]
                )

    def __apply_hyperlinks_to_content(
        self, content: List[str], hyperlinks: List[EncodedHyperlink]
    ) -> List[str]:
        encoded: List[str] = content.copy()

        for hyperlink in hyperlinks:
            index: int = hyperlink["index"]

            encoded[index] = content[index].replace(
                hyperlink["placeholder"], hyperlink["hyperlink"]
            )

        return encoded

    def __detect_trims(self) -> None:
        for posIndex in range(len(self.POSITIONS) - 1, -1, -1):
            position = self.POSITIONS[posIndex]
            position_content = getattr(self, position)

            if "content" in position_content.keys():
                self.trimer.analyse(position_content["content"], position)

    def __trim(self) -> None:
        for position in self.POSITIONS:
            if self.trimer.should_be_trimed(position):
                styled_content = getattr(self, position)["styled_content"]

                getattr(self, position)["styled_content"] = self.trimer.trim(
                    styled_content, position
                )

    def spark(self, end="\n"):
        self.__detect_hyperlinks()

        raw: str = self.raw()
        to_trim: int = len(raw) - self.get_width()

        if to_trim > 0:
            self.trimer = Trimer()
            self.trimer.target(to_trim)
            self.__detect_trims()
        elif self.is_full_width:
            self.__take_full_width()

        self.__apply_hyperlinks()

        self.mode = "color"
        print(self.render(), end=end)

    def raw(self) -> str:
        self.mode = "raw"
        return self.render()

    def __repr__(self) -> str:
        return self.render()
