from termspark.helpers.hex import HEX


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
