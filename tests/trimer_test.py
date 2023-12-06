from termspark.trimer.trimer import Trimer


class TestTrimer:
    def test_analyse_one_element(self):
        content = [" Termspark "]
        trimer = Trimer()
        trimer.target(6)
        analyse = trimer.analyse(content)

        assert analyse == {0: "spark "}

    def test_analyse_target_less_than_one_element_length(self):
        content = [" * ", " Termspark "]
        trimer = Trimer()
        trimer.target(3)
        analyse = trimer.analyse(content)

        assert analyse == {1: "rk "}

    def test_analyse_target_exceeds_one_element_length(self):
        content = [" * ", " Termspark "]
        trimer = Trimer()
        trimer.target(12)
        analyse = trimer.analyse(content)

        assert analyse == {0: " ", 1: " Termspark "}
