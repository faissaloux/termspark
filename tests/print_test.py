import pytest
from mock import patch  # type: ignore

from termspark import print
from termspark.exceptions.positionNotSupportedException import (
    PositionNotSupportedException,
)


class TestPrint:
    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.spark_left")
    def test_print_calls_spark_left_as_default(self, spark_left, spark):
        print("Termspark")

        spark_left.assert_called_once_with(["Termspark", None, None, None])
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.spark_left")
    def test_print_with_no_content(self, spark_left, spark):
        print()

        spark_left.assert_called_once_with(["", None, None, None])
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.spark_left")
    def test_print_with_some_parameters(self, spark_left, spark):
        print("Termspark", "white", style="italic, bold")

        spark_left.assert_called_once_with(["Termspark", "white", None, "italic, bold"])
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.spark_left")
    def test_print_with_all_parameters(self, spark_left, spark):
        print("Termspark", "white", "blue", "italic, bold")

        spark_left.assert_called_once_with(
            ["Termspark", "white", "blue", "italic, bold"]
        )
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.spark_right")
    def test_print_with_position(self, spark_right, spark):
        print("Termspark", "white", "blue", "italic, bold", position="right")

        spark_right.assert_called_once_with(
            ["Termspark", "white", "blue", "italic, bold"]
        )
        spark.assert_called_once_with()

    def test_print_raise_exception_on_unsupported_position(self):
        with pytest.raises(PositionNotSupportedException):
            print("Termspark", "white", "blue", "italic, bold", position="unsupported")
