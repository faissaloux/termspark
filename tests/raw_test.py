from termspark.termspark import TermSpark


class TestRaw:
    def test_raw_with_print(self):
        termspark = TermSpark().print_left("LEFT", "red").print_right("RIGHT", "blue")
        raw = termspark.raw()

        assert termspark.mode == "raw"
        assert len(raw) == termspark.get_width()

    def test_raw_with_spark(self):
        termspark = TermSpark().spark_left("LEFT", "red").spark_right("RIGHT", "blue")
        raw = termspark.raw()

        assert termspark.mode == "raw"
        assert len(raw) == termspark.get_width()

    def test_raw_with_one_side_multiple_content_with_odd_length(self):
        termspark = TermSpark()
        termspark.spark_center([" * ", "gray", "white"])
        termspark.spark_center([" Info ", "white", "blue"])
        raw = termspark.raw()

        width = termspark.get_width()
        separator_length = width - len(" *  INFO ")

        assert termspark.mode == "raw"
        assert len(raw) == width
        assert raw == " " * (separator_length // 2 + 1) + " *  Info " + " " * (
            separator_length // 2
        )

    def test_raw_with_multiple_side_content(self):
        termspark = TermSpark()
        termspark.spark_left([" LEFT ", "white", "blue"])
        termspark.spark_center([" * ", "gray", "white"])
        termspark.spark_center([" Info ", "white", "blue"])
        termspark.spark_right([" RIGHT ", "white", "blue"])
        termspark.set_separator(".")
        raw = termspark.raw()

        width = termspark.get_width()
        separator_length = width - len(" LEFT  *  INFO  RIGHT ")

        assert termspark.mode == "raw"
        assert len(raw) == width
        assert (
            raw
            == " LEFT "
            + "." * (separator_length // 2)
            + " *  Info "
            + "." * (separator_length // 2)
            + " RIGHT "
        )
