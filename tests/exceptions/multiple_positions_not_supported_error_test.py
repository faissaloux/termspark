from termspark.exceptions.multiple_positions_not_supported_error import (
    MultiplePositionsNotSupportedError,
)
from termspark.painter.constants.fore import Fore


class TestMultiplePositionsNotSupportedError:
    def test_exception_message(self):
        exception = MultiplePositionsNotSupportedError()
        assert all(
            word in str(exception)
            for word in [
                "full_width() can only be used with one position!",
                str(Fore.RED),
            ]
        )
