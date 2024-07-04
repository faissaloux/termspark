from termspark.exceptions.empty_error import EmptyError


class TestEmptyError:
    def test_exception_message(self):
        exception = EmptyError()
        assert all(
            word in str(exception)
            for word in [
                "can't be empty! Set a line or fill content.",
                "255;0;0",  # Red.
            ]
        )
