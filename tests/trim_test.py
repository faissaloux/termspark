from termspark.termspark import TermSpark


class TestTrim:
    def test_trim_when_text_exceeds_terminal_width(self):
        termspark = TermSpark()
        terminal_width = termspark.get_terminal_width()

        text = "A" * (terminal_width + 10)
        termspark = termspark.print_left("A" * 8).print_right(text, "red")
        termspark.spark()

        assert len(text) > len(termspark.left["content"][0])

    def test_trim_when_text_exceeds_terminal_width_on_list(self):
        termspark = TermSpark()
        terminal_width = termspark.get_terminal_width()

        text = "A" * (terminal_width + 10)
        termspark = termspark.spark_left(["A" * 8]).spark_right(
            [text, "red"], [text, "blue"]
        )
        termspark.spark()

        assert len(text) > len(termspark.left["content"][0])
