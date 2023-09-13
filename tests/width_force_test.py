from termspark.termspark import TermSpark


class TestForceWidth:
    def test_force_width(self):
        termspark = TermSpark().set_width(100).print_left("LEFT", "red")
        termspark.raw()

        assert termspark.get_width() == 100
        assert termspark.width == 100
