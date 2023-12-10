from termspark.exceptions.position_not_supported_error import PositionNotSupportedError
from termspark.painter.constants.fore import Fore


class TestPositionNotSupportedError:
    def test_exception_attributes(self):
        exception = PositionNotSupportedError("not_supported")
        assert exception.position == "not_supported"

    def test_exception_dynamic_message(self):
        exception = PositionNotSupportedError("not_supported")
        assert all(
            word in str(exception)
            for word in [
                f"{exception.position} position is not supported!",
                str(Fore.RED),
            ]
        )
