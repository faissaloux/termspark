from termspark.termspark import TermSpark


class TestTrim:
    def test_trim_when_text_exceeds_terminal_width(self):
        termspark = TermSpark()
        terminal_width = termspark.get_terminal_width()

        text = "A" * (terminal_width + 10)
        termspark = termspark.print_left(text, "red")
        termspark.spark()

        assert len(text) > len(termspark.left["content"][0])
