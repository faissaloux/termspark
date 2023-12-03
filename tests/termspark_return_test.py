import pytest

from termspark.exceptions.combinationException import CombinationException
from termspark.exceptions.emptyException import EmptyException
from termspark.termspark import TermSpark


class TestTermsparkReturn:
    def test_print_left(self):
        termspark = TermSpark().print_left("LEFT")

        terminal_width = termspark.get_terminal_width()
        content_space = len("LEFT")
        rest_space = terminal_width - content_space

        assert str(termspark) == "LEFT" + " " * rest_space

    def test_print_left_with_separator(self):
        termspark = TermSpark().print_left("LEFT").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("LEFT")
        rest_space = terminal_width - content_space

        assert str(termspark) == "LEFT" + "." * rest_space

    def test_print_right(self):
        termspark = TermSpark().print_right("RIGHT")

        terminal_width = termspark.get_terminal_width()
        content_space = len("RIGHT")
        rest_space = terminal_width - content_space

        assert str(termspark) == " " * rest_space + "RIGHT"

    def test_print_right_with_separator(self):
        termspark = TermSpark().print_right("RIGHT").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("RIGHT")
        rest_space = terminal_width - content_space

        assert str(termspark) == "." * rest_space + "RIGHT"

    def test_print_center(self):
        termspark = TermSpark().print_center("CENTER")

        terminal_width = termspark.get_terminal_width()
        content_space = len("CENTER")
        rest_space = terminal_width - content_space

        assert str(termspark) == " " * int(rest_space / 2) + "CENTER" + " " * int(
            rest_space / 2
        )

    def test_print_center_with_separator(self):
        termspark = TermSpark().print_center("CENTER").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("CENTER")
        rest_space = terminal_width - content_space

        assert str(termspark) == "." * int(rest_space / 2) + "CENTER" + "." * int(
            rest_space / 2
        )

    def test_combine_left_with_right(self):
        termspark = TermSpark().print_left("LEFT").print_right("RIGHT")

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        right_content_space = len("RIGHT")
        rest_space = terminal_width - left_content_space - right_content_space

        assert str(termspark) == "LEFT" + " " * rest_space + "RIGHT"

    def test_combine_left_with_right_with_separator(self):
        termspark = (
            TermSpark().print_left("LEFT").print_right("RIGHT").set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        right_content_space = len("RIGHT")
        rest_space = terminal_width - left_content_space - right_content_space

        assert str(termspark) == "LEFT" + "." * rest_space + "RIGHT"

    def test_combine_left_with_center(self):
        termspark = TermSpark().print_left("LEFT").print_center("CENTER")

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        center_content_space = len("CENTER")
        rest_space = terminal_width - left_content_space - center_content_space

        assert str(termspark) == "LEFT" + " " * int(
            rest_space / 2
        ) + "CENTER" + " " * int(rest_space / 2)

    def test_combine_left_with_center_with_separator(self):
        termspark = (
            TermSpark().print_left("LEFT").print_center("CENTER").set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        center_content_space = len("CENTER")
        rest_space = terminal_width - left_content_space - center_content_space

        assert str(termspark) == "LEFT" + "." * int(
            rest_space / 2
        ) + "CENTER" + "." * int(rest_space / 2)

    def test_combine_right_with_center(self):
        termspark = TermSpark().print_right("RIGHT").print_center("CENTER")

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("CENTER")
        rest_space = terminal_width - right_content_space - center_content_space

        assert (
            str(termspark)
            == " " * int(rest_space / 2)
            + "CENTER"
            + " " * int(rest_space / 2)
            + "RIGHT"
        )

    def test_combine_right_with_center_with_separator(self):
        termspark = (
            TermSpark().print_right("RIGHT").print_center("CENTER").set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("CENTER")
        rest_space = terminal_width - right_content_space - center_content_space

        assert (
            str(termspark)
            == "." * int(rest_space / 2)
            + "CENTER"
            + "." * int(rest_space / 2)
            + "RIGHT"
        )

    def test_combine_all(self):
        termspark = (
            TermSpark().print_left("LEFT").print_right("RIGHT").print_center("CENTER")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("CENTER")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert (
            str(termspark)
            == "LEFT"
            + " " * int(rest_space / 2)
            + "CENTER"
            + " " * int(rest_space / 2)
            + "RIGHT"
        )

    def test_combine_all_with_separator(self):
        termspark = (
            TermSpark()
            .print_left("LEFT")
            .print_right("RIGHT")
            .print_center("CENTER")
            .set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("CENTER")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert (
            str(termspark)
            == "LEFT"
            + "." * int(rest_space / 2)
            + "CENTER"
            + "." * int(rest_space / 2)
            + "RIGHT"
        )

    def test_can_call_functions_separately(self):
        termspark = TermSpark()
        termspark.print_left("LEFT")
        termspark.print_right("RIGHT")
        termspark.print_center("CENTER")
        termspark.set_separator(".")
        termspark.spark()

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("CENTER")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert (
            str(termspark)
            == "LEFT"
            + "." * int(rest_space / 2)
            + "CENTER"
            + "." * int(rest_space / 2)
            + "RIGHT"
        )

    def test_can_chain_multiple_same_position_spark(self):
        termspark = TermSpark()
        termspark.spark_left(["*"])
        termspark.spark_left("LEFT")
        termspark.spark_right("*")
        termspark.spark_right(["RIGHT"])
        termspark.spark_center("CENTER")
        termspark.set_separator(".")
        termspark.spark()

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT") + len("*")
        center_content_space = len("CENTER")
        left_content_space = len("LEFT") + len("*")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert (
            str(termspark)
            == "*LEFT"
            + "." * int(rest_space / 2)
            + "CENTER"
            + "." * int(rest_space / 2)
            + "*RIGHT"
        )

    def test_default_line(self):
        termspark = TermSpark().line()

        terminal_width = termspark.get_terminal_width()
        assert str(termspark) == " " * terminal_width

    def test_customized_line(self):
        termspark = TermSpark().line(".")

        terminal_width = termspark.get_terminal_width()
        assert str(termspark) == "." * terminal_width

    def test_customized_line_with_highlight(self):
        termspark = TermSpark().line(".", "green")

        terminal_width = termspark.get_terminal_width()
        assert str(termspark) == "\x1b[42m.\x1b[0m" * terminal_width

    def test_force_width(self):
        width = 100
        termspark = TermSpark().set_width(width).line(".")

        assert str(termspark) == "." * width

    def test_cant_combine_line_with_separator(self):
        termspark = TermSpark()
        termspark.print_left("LEFT")
        termspark.set_separator(".")
        termspark.line(".")

        with pytest.raises(CombinationException):
            termspark.spark()

    def test_cant_spark_without_content(self):
        termspark = TermSpark()

        with pytest.raises(EmptyException):
            termspark.spark()

    def test_cant_spark_separator_without_content_in_line(self):
        termspark = TermSpark()
        termspark.set_separator(".")

        with pytest.raises(EmptyException):
            termspark.spark()
