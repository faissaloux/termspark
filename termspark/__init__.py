import os
import sys
from typing import Optional

from termspark.termspark import TermSpark

if sys.platform == "win32":  # codecov-ignore
    os.system("color")


def print(
    content: Optional[str] = None,
    color: Optional[str] = None,
    highlight: Optional[str] = None,
    style: Optional[str] = None,
) -> None:
    if content is None:
        content = ""

    termspark = TermSpark()
    termspark.spark_left([content, color, highlight, style])  # type: ignore
    termspark.spark()
