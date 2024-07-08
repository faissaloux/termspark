from termspark.helpers.rgb import RGB


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
