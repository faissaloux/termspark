import termspark.termspark


class LenNotSupportedError(Exception):
    def __init__(self, var: str, length: int):
        self.var = var
        self.length = length

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"{self.var} must contain {self.length} character!",
            "red",
        )
        return str(message)
