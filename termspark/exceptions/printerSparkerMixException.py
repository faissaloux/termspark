import termspark.termspark


class PrinterSparkerMixException(Exception):
    def __init__(self, position: str):
        self.position = position

    def __str__(self):
        message = termspark.TermSpark()
        message = message.spark_left(
            ["can't use ", "red"],
            [f" print_{self.position}() ", "white", "red"],
            [" with ", "red"],
            [f" spark_{self.position}() \n\n", "white", "red"],
        )
        message = message.spark_left(
            [" you can replace ", "blue"],
            [f" print_{self.position}() ", "white", "red"],
            [" with ", "blue"],
            [f" spark_{self.position}() ", "white", "blue"],
        )
        return str(message)
