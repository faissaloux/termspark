from typing import Sequence


class List:
    def snake(self, elements: Sequence[str | Sequence[str]]) -> Sequence[str]:
        snakeElements: Sequence[str] = []
        for index, elem in enumerate(elements):
            if isinstance(elem, Sequence):
                self.snake(elem)
            else:
                snakeElements[index] = elem.replace(" ", "_") if elem else elem

        return snakeElements
