import termspark.termspark


class MinNotReachedError(Exception):
    def __init__(self, var: str, min: int):
        self.var = var
        self.min = min

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"{self.var} must be at least {self.min}!", "red"
        )
        return str(message)
