from termspark.exceptions.parameter_type_error import ParameterTypeError
from termspark.painter.constants.fore import Fore


class TestParameterTypeError:
    def test_exception_attributes(self):
        exception = ParameterTypeError("function", "parameter", str, int)

        assert exception.function == "function"
        assert exception.parameter == "parameter"
        assert exception.current == str
        assert exception.expected == int

    def test_exception_dynamic_message(self):
        left_exception = ParameterTypeError("function", "parameter", str, int)
        assert all(
            word in str(left_exception)
            for word in [
                f"You have passed {str} to function(parameter=), expected {int}.",
                str(Fore.RED),
            ]
        )
