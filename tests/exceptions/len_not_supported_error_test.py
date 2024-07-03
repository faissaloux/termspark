from termspark.exceptions.len_not_supported_error import LenNotSupportedError


class TestLenNotSupportedError:
    def test_exception_attributes(self):
        exception = LenNotSupportedError("separator", 1)
        assert exception.var == "separator"
        assert exception.length == 1

    def test_exception_dynamic_message(self):
        exception = LenNotSupportedError("separator", 1)
        assert all(
            word in str(exception)
            for word in [
                f"{exception.var} must contain {exception.length} character!",
                "255;0;0",  # Red.
            ]
        )
