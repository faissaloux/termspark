from termspark.exceptions.combination_error import CombinationError
from termspark.painter.constants.fore import Fore


class TestCombinationError:
    def test_exception_attributes(self):
        exception = CombinationError("line", "separator")
        assert exception.elements == ("line", "separator")

    def test_exception_dynamic_message(self):
        exception = CombinationError("line", "separator")
        assert all(
            word in str(exception)
            for word in [
                f"can't combine ('line', 'separator')",
                str(Fore.RED),
            ]
        )
