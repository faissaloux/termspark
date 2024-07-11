from termspark.painter.modes.name import Name


class TestName:
    def test_format(self):
        assert Name("blue").format() == "0;0;255"
        assert Name("white").format() == "255;255;255"
        assert Name("black").format() == "0;0;0"
        assert Name("JAPANESE_LAUREL").format() == "0;135;0"
        assert Name("japanese_laurel").format() == "0;135;0"
