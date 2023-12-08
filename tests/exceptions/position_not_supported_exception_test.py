from termspark.exceptions.positionNotSupportedException import (
    PositionNotSupportedException,
)
from termspark.painter.constants.fore import Fore


class TestPositionNotSupportedException:
    def test_exception_attributes(self):
        exception = PositionNotSupportedException("not_supported")
        assert exception.position == "not_supported"

    def test_exception_dynamic_message(self):
        exception = PositionNotSupportedException("not_supported")
        assert all(
            word in str(exception)
            for word in [
                f"{exception.position} position is not supported!",
                str(Fore.RED),
            ]
        )
