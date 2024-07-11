from termspark.painter.modes.rgb import RGB


class TestRGB:
    def test_check(self):
        assert RGB.check("36,114,200")
        assert RGB.check((36, 114, 200))
        assert RGB.check(None) == False
        assert RGB.check("") == False
        assert RGB.check((36, 114)) == False
        assert RGB.check((36, 114, 200, 114)) == False
        assert RGB.check((36, 114, 256)) == False
        assert RGB.check("36,114") == False

    def test_to_str(self):
        assert RGB.to_str("36,114,200") == "36,114,200"
        assert RGB.to_str((36, 114, 200)) == "36,114,200"

    def test_format(self):
        assert RGB("36,114,200").format() == "36;114;200"
        assert RGB("36,_114,_200").format() == "36;114;200"
        assert RGB("__36,_114____,_____200__").format() == "36;114;200"
        assert RGB("36,114").format() == False
        assert RGB("#2472C8").format() == False
        assert RGB("blue").format() == False
