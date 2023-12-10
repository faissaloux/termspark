import termspark.termspark


class CombinationError(Exception):
    def __init__(self, *elements: str):
        self.elements = elements

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"can't combine {self.elements}",
            "red",
        )

        return str(message)
