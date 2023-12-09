from termspark.line.line import Line
from termspark.structurer.structurer import Form


class Separator(Line):
    __length: int

    def __init__(self, data: Form):
        super().__init__(data)

    def set_length(self, length: int) -> None:
        self.__length = length

    def get_length(self) -> int:
        return self.__length
