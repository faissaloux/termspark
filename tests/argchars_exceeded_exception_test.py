from termspark.exceptions.argCharsExceededException import ArgCharsExceededException
from termspark.painter.constants.fore import Fore

class TestArgCharsExceededException:
    def test_exception_attributes(self):
        exception = ArgCharsExceededException('separator', 'one')
        assert exception.arg == 'separator'
        assert exception.max == 'one'

    def test_exception_dynamic_message(self):
        left_exception = ArgCharsExceededException('separator', 'one')
        assert all(word in str(left_exception) for word in ['Sorry, separator can contain only one character', str(Fore.RED)])

        center_exception = ArgCharsExceededException('separator', 'three')
        assert all(word in str(center_exception) for word in ['Sorry, separator can contain only three character', str(Fore.RED)])

        right_exception = ArgCharsExceededException('line', 'three')
        assert all(word in str(right_exception) for word in ['Sorry, line can contain only three character', str(Fore.RED)])