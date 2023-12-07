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
    end: str = "\n",
) -> None:
    if content is None:
        content = ""

    termspark = TermSpark()
    termspark.print_left(content, color, highlight, style)
    termspark.spark(end)
