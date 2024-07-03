from termspark.exceptions.min_not_reached_error import MinNotReachedError


class TestMinNotReachedError:
    def test_exception_attributes(self):
        exception = MinNotReachedError("max", 1)
        assert exception.var == "max"
        assert exception.min == 1

    def test_exception_dynamic_message(self):
        exception = MinNotReachedError("max", 1)
        assert all(
            word in str(exception)
            for word in [
                "max must be at least 1!",
                "255;0;0",  # Red.
            ]
        )
