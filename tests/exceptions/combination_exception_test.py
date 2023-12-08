from termspark.exceptions.combinationException import CombinationException
from termspark.painter.constants.fore import Fore


class TestCombinationException:
    def test_exception_attributes(self):
        exception = CombinationException("line", "separator")
        assert exception.elements == ("line", "separator")

    def test_exception_dynamic_message(self):
        exception = CombinationException("line", "separator")
        assert all(
            word in str(exception)
            for word in [
                f"can't combine ('line', 'separator')",
                str(Fore.RED),
            ]
        )
