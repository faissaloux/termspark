from termspark.exceptions.emptyException import EmptyException
from termspark.painter.constants.fore import Fore


class TestEmptyException:
    def test_exception_message(self):
        exception = EmptyException()
        assert all(
            word in str(exception)
            for word in [
                "can't be empty! Set a line or fill content.",
                str(Fore.RED),
            ]
        )
