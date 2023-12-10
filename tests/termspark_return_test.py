import pytest

from termspark.exceptions.combination_error import CombinationError
from termspark.exceptions.empty_error import EmptyError
from termspark.hyperlink.hyperlink import Hyperlink
from termspark.termspark import TermSpark


class TestTermsparkReturn:
    def test_print_left(self):
        termspark = TermSpark().print_left("LEFT")

        terminal_width = termspark.get_terminal_width()
        content_space = len("LEFT")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "LEFT" + " " * rest_space

    def test_print_left_with_separator(self):
        termspark = TermSpark().print_left("LEFT").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("LEFT")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "LEFT" + "." * rest_space

    def test_print_right(self):
        termspark = TermSpark().print_right("RIGHT")

        terminal_width = termspark.get_terminal_width()
        content_space = len("RIGHT")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == " " * rest_space + "RIGHT"

    def test_print_right_with_separator(self):
        termspark = TermSpark().print_right("RIGHT").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("RIGHT")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "." * rest_space + "RIGHT"

    def test_print_center(self):
        termspark = TermSpark().print_center("CENTER")

        terminal_width = termspark.get_terminal_width()
        content_space = len("CENTER")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == " " * int(rest_space / 2) + "CENTER" + " " * int(
            rest_space / 2
        )

    def test_print_center_with_separator(self):
        termspark = TermSpark().print_center("CENTER").set_separator(".")

        terminal_width = termspark.get_terminal_width()
        content_space = len("CENTER")
        rest_space = terminal_width - content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "." * int(rest_space / 2) + "CENTER" + "." * int(
            rest_space / 2
        )

    def test_combine_left_with_right(self):
        termspark = TermSpark().print_left("LEFT").print_right("RIGHT")

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        right_content_space = len("RIGHT")
        rest_space = terminal_width - left_content_space - right_content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "LEFT" + " " * rest_space + "RIGHT"

    def test_combine_left_with_right_with_separator(self):
        termspark = (
            TermSpark().print_left("LEFT").print_right("RIGHT").set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        right_content_space = len("RIGHT")
        rest_space = terminal_width - left_content_space - right_content_space

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "LEFT" + "." * rest_space + "RIGHT"

    def test_combine_left_with_center(self):
        termspark = TermSpark().print_left("LEFT").print_center("CENTER")

        terminal_width = termspark.get_terminal_width()
        left_content_space = len("LEFT")
        center_content_space = len("CENTER")
        rest_space = terminal_width - left_content_space - center_content_space

        assert terminal_width == len(str(termspark))
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

        assert terminal_width == len(str(termspark))
        assert str(termspark) == "LEFT" + "." * int(
            rest_space / 2
        ) + "CENTER" + "." * int(rest_space / 2)

    def test_combine_right_with_center(self):
        termspark = TermSpark().print_right(" RIGHT ").print_center(" TERMSPARK ")

        terminal_width = termspark.get_terminal_width()
        right_content_space = len(" RIGHT ")
        center_content_space = len(" TERMSPARK ")
        rest_space = terminal_width - right_content_space - center_content_space

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == " " * int(rest_space / 2)
            + " TERMSPARK "
            + " " * int(rest_space / 2)
            + " RIGHT "
        )

    def test_combine_right_with_center_with_separator(self):
        termspark = (
            TermSpark()
            .print_right(" RIGHT ")
            .print_center(" TERMSPARK ")
            .set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len(" RIGHT ")
        center_content_space = len(" TERMSPARK ")
        rest_space = terminal_width - right_content_space - center_content_space

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "." * int(rest_space / 2)
            + " TERMSPARK "
            + "." * int(rest_space / 2)
            + " RIGHT "
        )

    def test_combine_all(self):
        termspark = (
            TermSpark()
            .print_left("LEFT")
            .print_right("RIGHT")
            .print_center("TERMSPARK")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("TERMSPARK")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "LEFT"
            + " " * int(rest_space / 2)
            + "TERMSPARK"
            + " " * int(rest_space / 2)
            + "RIGHT"
        )

    def test_combine_all_with_odd_separator_length(self):
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

        assert rest_space % 2 != 0
        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "LEFT"
            + " " * int(rest_space / 2 + 1)
            + "CENTER"
            + " " * int(rest_space / 2)
            + "RIGHT"
        )

    def test_combine_all_with_separator(self):
        termspark = (
            TermSpark()
            .print_left("LEFT")
            .print_right("RIGHT")
            .print_center("TERMSPARK")
            .set_separator(".")
        )

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("TERMSPARK")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "LEFT"
            + "." * int(rest_space / 2)
            + "TERMSPARK"
            + "." * int(rest_space / 2)
            + "RIGHT"
        )

    def test_can_call_functions_separately(self):
        termspark = TermSpark()
        termspark.print_left("LEFT")
        termspark.print_right("RIGHT")
        termspark.print_center("TERMSPARK")
        termspark.set_separator(".")
        termspark.spark()

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT")
        center_content_space = len("TERMSPARK")
        left_content_space = len("LEFT")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "LEFT"
            + "." * int(rest_space / 2)
            + "TERMSPARK"
            + "." * int(rest_space / 2)
            + "RIGHT"
        )

    def test_can_chain_multiple_same_position_spark(self):
        termspark = TermSpark()
        termspark.spark_left(["*"])
        termspark.spark_left("LEFT")
        termspark.spark_right("*")
        termspark.spark_right(["RIGHT"])
        termspark.spark_center("TERMSPARK")
        termspark.set_separator(".")
        termspark.spark()

        terminal_width = termspark.get_terminal_width()
        right_content_space = len("RIGHT") + len("*")
        center_content_space = len("TERMSPARK")
        left_content_space = len("LEFT") + len("*")
        rest_space = (
            terminal_width
            - left_content_space
            - right_content_space
            - center_content_space
        )

        assert terminal_width == len(str(termspark))
        assert (
            str(termspark)
            == "*LEFT"
            + "." * int(rest_space / 2)
            + "TERMSPARK"
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

        with pytest.raises(CombinationError):
            termspark.spark()

    def test_cant_spark_without_content(self):
        termspark = TermSpark()

        with pytest.raises(EmptyError):
            termspark.spark()

    def test_cant_spark_separator_without_content_in_line(self):
        termspark = TermSpark()
        termspark.set_separator(".")

        with pytest.raises(EmptyError):
            termspark.spark()

    def test_contnt_includes_hyperlink(self):
        termspark = TermSpark()
        termspark.print_left(" REPOSITOTY ")
        termspark.print_right(" [termspark](https://github.com/faissaloux/termspark) ")
        termspark.set_separator(".")
        termspark.spark()

        terminal_width = termspark.get_terminal_width()
        left_content_space = len(" REPOSITOTY ")
        right_content_space = len("termspark") + len("  ")
        rest_space = terminal_width - left_content_space - right_content_space

        assert (
            str(termspark)
            == " REPOSITOTY "
            + "." * int(rest_space)
            + " "
            + Hyperlink.HYPERLINK_PREFIX
            + "https://github.com/faissaloux/termspark"
            + "\x1b\\"
            + "termspark"
            + Hyperlink.HYPERLINK_SUFFIX
            + "\x1b\\"
            + " "
        )
