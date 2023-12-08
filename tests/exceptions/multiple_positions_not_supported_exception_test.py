from termspark.exceptions.multiplePositionsNotSupported import (
    MultiplePositionsNotSupported,
)
from termspark.painter.constants.fore import Fore


class TestMultiplePositionsNotSupportedException:
    def test_exception_message(self):
        exception = MultiplePositionsNotSupported()
        assert all(
            word in str(exception)
            for word in [
                "full_width() can only be used with one position!",
                str(Fore.RED),
            ]
        )
