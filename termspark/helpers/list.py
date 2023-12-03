from typing import Sequence


class List:
    def snake(self, elements: Sequence[str | Sequence[str]]) -> Sequence[str]:
        snakeElements: Sequence[str] = []

        for index, elem in enumerate(elements):
            if isinstance(elem, list):
                snakeElements.insert(index, self.snake(elem))  # type: ignore
            else:
                snakeElements.insert(index, elem.replace(" ", "_") if elem else elem)  # type: ignore

        return snakeElements
