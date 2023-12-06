from termspark.trimer.trimer import Trimer


class TestTrimer:
    def test_analyse_one_element(self):
        content = [" Termspark "]
        trimer = Trimer()
        trimer.target(6)
        analyse = trimer.analyse(content, "left")

        assert analyse == {"left": {0: "spark "}}

    def test_analyse_target_less_than_one_element_length(self):
        content = [" * ", " Termspark "]
        trimer = Trimer()
        trimer.target(3)
        analyse = trimer.analyse(content, "right")

        assert analyse == {"right": {1: "rk "}}

    def test_analyse_target_exceeds_one_element_length(self):
        content = [" * ", " Termspark "]
        trimer = Trimer()
        trimer.target(12)
        analyse = trimer.analyse(content, "center")

        assert analyse == {"center": {0: " ", 1: " Termspark "}}

    def test_should_be_trimed(self):
        left_content = [" * ", " Author "]
        right_content = [" * ", " right "]
        trimer = Trimer()
        trimer.target(13)
        trimer.analyse(left_content, "left")
        trimer.analyse(right_content, "right")

        assert trimer.should_be_trimed("left")
        assert trimer.should_be_trimed("right")
        assert not trimer.should_be_trimed("center")

    def test_trim(self):
        content = [" *  ", " Termspark "]
        trimer = Trimer()
        trimer.target(6)
        trimer.analyse(content, "left")

        assert trimer.trim(" *  Termspark ", "left") == " *  Term"
