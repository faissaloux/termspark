import os
import sys
import types
from builtins import type as builtinType
from typing import Callable, Optional

from termspark.exceptions.parameter_type_error import ParameterTypeError
from termspark.exceptions.position_not_supported_error import PositionNotSupportedError
from termspark.termspark import TermSpark

if sys.platform == "win32":  # codecov-ignore
    os.system("color")


def print(
    content: Optional[str] = None,
    color: Optional[str] = None,
    highlight: Optional[str] = None,
    style: Optional[str] = None,
    position: str = "left",
    full_width: bool = False,
) -> None:
    if content is None:
        content = ""

    termspark = TermSpark()

    if not hasattr(termspark, f"spark_{position}"):
        raise PositionNotSupportedError(position)

    if full_width:
        termspark.full_width()

    spark = getattr(termspark, f"spark_{position}")

    spark([content, color, highlight, style])  # type: ignore
    termspark.spark()


def line(pattern: Optional[str] = None, highlight: Optional[str] = None) -> None:
    termspark = TermSpark()
    termspark.line(pattern, highlight)
    termspark.spark()


def input(
    prompt: Optional[str] = None,
    color: Optional[str] = None,
    highlight: Optional[str] = None,
    style: Optional[str] = None,
    position: str = "left",
    full_width: bool = False,
    type: builtinType = str,
    callback: Callable = lambda prompt: prompt,
):
    if builtinType(type) != builtinType:
        raise ParameterTypeError("print", "type", builtinType(type), builtinType)

    if builtinType(callback) != types.FunctionType:
        raise ParameterTypeError(
            "print", "callback", builtinType(type), types.FunctionType
        )

    print(prompt, color, highlight, style, position, full_width)

    scaned = type(sys.stdin.readline().rstrip("\n"))

    return callback(scaned)
