from typing import Sequence, Union

from ..painter.modes.rgb import RGB


class List:
    def snake(self, elements: Sequence[Union[str, Sequence[str]]]) -> Sequence[str]:
        snakeElements: Sequence[str] = []

        for index, elem in enumerate(elements):
            if isinstance(elem, list):
                snakeElements.insert(index, self.snake(elem))  # type: ignore
            else:
                if RGB.check(elem):
                    snakeElements.insert(index, elem)  # type: ignore
                    continue

                snakeElements.insert(index, elem.replace(" ", "_") if elem else elem)  # type: ignore

        return snakeElements
