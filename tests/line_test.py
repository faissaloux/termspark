from mock import patch  # type: ignore

from termspark import line


class TestLine:
    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.line")
    def test_line_calls_empty_line(self, termspark_line, spark):
        line()

        termspark_line.assert_called_once_with(None, None)
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.line")
    def test_line_with_pattern(self, termspark_line, spark):
        line(".")

        termspark_line.assert_called_once_with(".", None)
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.line")
    def test_line_with_pattern_and_highlight(self, termspark_line, spark):
        line(".", "blue")

        termspark_line.assert_called_once_with(".", "blue")
        spark.assert_called_once_with()

    @patch("termspark.termspark.TermSpark.spark")
    @patch("termspark.termspark.TermSpark.line")
    def test_line_with_only_highlight(self, termspark_line, spark):
        line(highlight="blue")

        termspark_line.assert_called_once_with(None, "blue")
        spark.assert_called_once_with()
