import pytest
from mock import patch  # type: ignore

from termspark import input
from termspark.exceptions.parameter_type_error import ParameterTypeError


class TestInput:
    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_empty_input_calls_print_and_returns_scaned_input_with_defaults(self, print, readline):
        input()

        print.assert_called_once_with(None, None, None, None, "left", None, False)
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_with_prompt(self, print, readline):
        input(" Enter your name: ")

        print.assert_called_once_with(" Enter your name: ", None, None, None, "left", None, False)
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_change_color(self, print, readline):
        input(" Enter your name: ", "blue")

        print.assert_called_once_with(" Enter your name: ", "blue", None, None, "left", None, False)
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_change_highlight(self, print, readline):
        input(" Enter your name: ", "white", "blue")

        print.assert_called_once_with(
            " Enter your name: ", "white", "blue", None, "left", None, False
        )
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_change_style(self, print, readline):
        input(" Enter your name: ", "white", "blue", "italic, bold")

        print.assert_called_once_with(
            " Enter your name: ", "white", "blue", "italic, bold", "left", None, False
        )
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_can_change_position(self, print, readline):
        input(" Enter your name: ", highlight="blue", position="center")

        print.assert_called_once_with(
            " Enter your name: ", None, "blue", None, "center", None, False
        )
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_can_set_separator(self, print, readline):
        input(" Enter your name: ", highlight="blue", position="center", separator=".")

        print.assert_called_once_with(
            " Enter your name: ", None, "blue", None, "center", ".", False
        )
        readline.assert_called_once_with()

    @patch("sys.stdin.readline")
    @patch("termspark.print")
    def test_input_can_take_full_width(self, print, readline):
        input(" Enter your name: ", highlight="blue", position="center", full_width=True)

        print.assert_called_once_with(
            " Enter your name: ", None, "blue", None, "center", None, True
        )
        readline.assert_called_once_with()

    def test_cant_set_type_to_input_callback(self):
        with pytest.raises(ParameterTypeError):
            input(" Enter your age: ", highlight="blue", position="center", callback=int)

    def test_cant_set_not_type_function_to_input_type(self):
        with pytest.raises(ParameterTypeError):
            input(" Enter your age: ", highlight="blue", position="center", type=len)
