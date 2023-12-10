import termspark.termspark


class ArgCharsExceededError(Exception):
    def __init__(self, arg: str, max: str):
        self.arg = arg
        self.max = max

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"Sorry, {self.arg} can contain only {self.max} character", "red"
        )
        return str(message)
