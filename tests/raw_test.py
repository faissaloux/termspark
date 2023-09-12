from termspark.termspark import TermSpark


class TestRaw:
    def test_raw(self):
        termspark = TermSpark().print_left("LEFT", "red")
        termspark.raw()

        assert termspark.mode == "raw"
