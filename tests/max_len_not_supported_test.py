from termspark.exceptions.maxLenNotSupported import MaxLenNotSupported
from termspark.painter.constants.fore import Fore


class TestMaxLenNotSupported:
    def test_exception_attributes(self):
        exception = MaxLenNotSupported("print_left")
        assert exception.method == "print_left"

    def test_exception_dynamic_message(self):
        exception = MaxLenNotSupported("print_right")
        assert all(
            word in str(exception)
            for word in [
                f"Max Length not supported for {exception.method}, use spark_[position] instead!",
                str(Fore.RED),
            ]
        )
