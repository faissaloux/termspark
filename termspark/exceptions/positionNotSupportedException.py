import termspark.termspark


class PositionNotSupportedException(Exception):
    def __init__(self, position: str):
        self.position = position

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"{self.position} position is not supported!",
            "red",
        )
        return str(message)
