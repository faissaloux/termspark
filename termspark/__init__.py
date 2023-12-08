import os
import sys
from typing import Optional

from termspark.exceptions.positionNotSupportedException import (
    PositionNotSupportedException,
)
from termspark.termspark import TermSpark

if sys.platform == "win32":  # codecov-ignore
    os.system("color")


def print(
    content: Optional[str] = None,
    color: Optional[str] = None,
    highlight: Optional[str] = None,
    style: Optional[str] = None,
    position: str = "left",
) -> None:
    if content is None:
        content = ""

    termspark = TermSpark()

    if not hasattr(termspark, f"spark_{position}"):
        raise PositionNotSupportedException(position)

    spark = getattr(termspark, f"spark_{position}")

    spark([content, color, highlight, style])  # type: ignore
    termspark.spark()
