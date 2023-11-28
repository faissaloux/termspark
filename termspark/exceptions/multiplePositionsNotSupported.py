import termspark.termspark


class MultiplePositionsNotSupported(Exception):
    def __str__(self):
        message = termspark.TermSpark().print_left(
            f"full_width() can only be used with one position!", "red"
        )

        return str(message)
