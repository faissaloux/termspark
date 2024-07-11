from termspark.painter.modes.hex import HEX


class TestHEX:
    def test_check(self):
        assert HEX.check("#000000")
        assert HEX.check("#ffffff")
        assert HEX.check("#FFFFFF")
        assert HEX.check("#2472c8")
        assert HEX.check("#2472C8")
        assert HEX.check("#000")
        assert HEX.check("#fff")
        assert HEX.check("#FFF")
        assert HEX.check("#ffg") == False
        assert HEX.check("#FFG") == False
        assert HEX.check("#FFFFFFF") == False
        assert HEX.check("#FF") == False
        assert HEX.check("#") == False
        assert HEX.check(None) == False
        assert HEX.check("") == False

    def test_to_rgb(self):
        assert HEX.to_rgb("#000000") == (0, 0, 0)
        assert HEX.to_rgb("#ffffff") == (255, 255, 255)
        assert HEX.to_rgb("#FFFFFF") == (255, 255, 255)
        assert HEX.to_rgb("#ffa") == (255, 255, 170)
        assert HEX.to_rgb("#2472c8") == (36, 114, 200)
        assert HEX.to_rgb("#2472C8") == (36, 114, 200)
        assert HEX.to_rgb("#000") == (0, 0, 0)
        assert HEX.to_rgb("#fff") == (255, 255, 255)
        assert HEX.to_rgb("#FFF") == (255, 255, 255)

    def test_format(self):
        assert HEX("#2472C8").format() == ("36;114;200")
        assert HEX("#FFF").format() == ("255;255;255")
