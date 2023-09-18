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
