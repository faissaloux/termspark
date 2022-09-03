class List:
    def snake(self, list: list[str]) -> list[str]:
        for index, elem in enumerate(list):
            list[index] = elem.replace(' ', '_') if elem else elem

        return list
