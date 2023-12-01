import pytest

from termspark.exceptions.multiplePositionsNotSupported import (
    MultiplePositionsNotSupported,
)
from termspark.termspark import TermSpark


class TestRaw:
    def test_is_full_width(self):
        termspark = TermSpark().print_left("LEFT", "red")
        termspark.full_width()

        assert termspark.is_full_width == True

    def test_full_width_does_not_accept_multiple_positions(self):
        termspark = TermSpark().spark_left("LEFT", "red").spark_right("RIGHT", "blue")
        termspark.full_width()

        with pytest.raises(MultiplePositionsNotSupported):
            termspark.spark()

    def test_is_full_width_with_spark_left(self):
        termspark = TermSpark().spark_left(["LEFT", "white", "blue"])
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.left["content"][0]) == termspark.get_terminal_width()

    def test_is_full_width_with_spark_center(self):
        termspark = TermSpark().spark_center(["CENTER", "white", "blue"])
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.center["content"][0]) == termspark.get_terminal_width()

    def test_is_full_width_with_spark_right(self):
        termspark = TermSpark().spark_right(["RIGHT", "white", "blue"])
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.right["content"][0]) == termspark.get_terminal_width()

    def test_is_full_width_with_print_left(self):
        termspark = TermSpark().print_left("LEFT", "white", "blue")
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.left["content"][0]) == termspark.get_terminal_width()

    def test_is_full_width_with_print_center(self):
        termspark = TermSpark().print_center("CENTER", "white", "blue")
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.center["content"][0]) == termspark.get_terminal_width()

    def test_is_full_width_with_print_right(self):
        termspark = TermSpark().print_right("RIGHT", "white", "blue")
        termspark.full_width()
        termspark.spark()

        assert termspark.is_full_width == True
        assert len(termspark.right["content"][0]) == termspark.get_terminal_width()
