from termspark.exceptions.empty_error import EmptyError
from termspark.painter.constants.fore import Fore


class TestEmptyError:
    def test_exception_message(self):
        exception = EmptyError()
        assert all(
            word in str(exception)
            for word in [
                "can't be empty! Set a line or fill content.",
                str(Fore.RED),
            ]
        )
