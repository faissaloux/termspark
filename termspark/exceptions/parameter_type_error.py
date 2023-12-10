import termspark.termspark


class ParameterTypeError(Exception):
    def __init__(self, function: str, parameter: str, current, expected):
        self.function: str = function
        self.parameter: str = parameter
        self.current = current
        self.expected = expected

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"You have passed {self.current} to {self.function}({self.parameter}=), expected {self.expected}.",
            "red",
        )

        return str(message)
