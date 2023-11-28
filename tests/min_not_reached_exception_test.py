from termspark.exceptions.minNotReachedException import MinNotReachedException
from termspark.painter.constants.fore import Fore


class TestMinNotReachedException:
    def test_exception_attributes(self):
        exception = MinNotReachedException("max", 1)
        assert exception.var == "max"
        assert exception.min == 1

    def test_exception_dynamic_message(self):
        exception = MinNotReachedException("max", 1)
        assert all(
            word in str(exception)
            for word in [
                "max must be at least 1!",
                str(Fore.RED),
            ]
        )
