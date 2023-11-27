import termspark.termspark


class MaxLenNotSupported(Exception):
    def __init__(self, method: str):
        self.method = method

    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"Max Length not supported for {self.method}, use spark_[position] instead!",
            "red",
        )
        return str(message)
