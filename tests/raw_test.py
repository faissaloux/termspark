from termspark.termspark import TermSpark


class TestRaw:
    def test_raw_with_print(self):
        termspark = TermSpark().print_left("LEFT", "red").print_right("RIGHT", "blue")
        termspark.raw()

        assert termspark.mode == "raw"

    def test_raw_with_spark(self):
        termspark = TermSpark().spark_left("LEFT", "red").spark_right("RIGHT", "blue")
        termspark.raw()

        assert termspark.mode == "raw"

    def test_raw_with_one_side_multiple_content(self):
        termspark = TermSpark()
        termspark.spark_center([" * ", "gray", "white"])
        termspark.spark_center([" Info ", "white", "blue"])
        termspark.raw()

        assert termspark.mode == "raw"
