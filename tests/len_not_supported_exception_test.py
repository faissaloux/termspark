from termspark.exceptions.lenNotSupportedException import LenNotSupportedException
from termspark.painter.constants.fore import Fore


class TestLenNotSupportedException:
    def test_exception_attributes(self):
        exception = LenNotSupportedException("separator", 1)
        assert exception.var == "separator"
        assert exception.length == 1

    def test_exception_dynamic_message(self):
        exception = LenNotSupportedException("separator", 1)
        assert all(
            word in str(exception)
            for word in [
                f"{exception.var} must contain {exception.length} character!",
                str(Fore.RED),
            ]
        )
