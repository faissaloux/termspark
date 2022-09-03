from typing import List as TypingList

class List:
    def snake(self, list: TypingList[str]) -> TypingList[str]:
        for index, elem in enumerate(list):
            list[index] = elem.replace(' ', '_') if elem else elem

        return list
