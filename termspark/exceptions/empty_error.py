import termspark.termspark


class EmptyError(Exception):
    def __str__(self):
        message = termspark.TermSpark().print_left(
            "can't be empty! Set a line or fill content.",
            "red",
        )

        return str(message)
