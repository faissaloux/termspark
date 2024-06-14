from termspark.hyperlink.hyperlink import Hyperlink


class TestHyperlink:
    def test_attributes(self):
        assert Hyperlink.HYPERLINK_PATTERN == "\\[([^\\[]*?)]\\(\\s*(http[s]?://[^)]+)\\s*\\)"
        assert Hyperlink.HYPERLINK_PREFIX == "\x1b]8;;"
        assert Hyperlink.HYPERLINK_SUFFIX == "\x1b]8;;"
        assert Hyperlink.RESET == "\x1b\\\\"

    def test_set_content(self):
        content = [" Link ", "[@faissaloux](https://github.com/faissaloux)"]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)

        assert hyperlink.content == content

    def test_exists_with_no_hyperlink(self):
        content = [" Link "]

        assert Hyperlink.exists_in(content) == {}

    def test_exists_with_one_hyperlink(self):
        content = [" Link ", "[@faissaloux](https://github.com/faissaloux)"]

        assert Hyperlink.exists_in(content) == {
            1: [("@faissaloux", "https://github.com/faissaloux")]
        }

    def test_exists_with_multiple_hyperlinks(self):
        content = [
            " [@termspark](https://github.com/faissaloux/termspark) ",
            "[@faissaloux](https://github.com/faissaloux)",
        ]

        assert Hyperlink.exists_in(content) == {
            0: [("@termspark", "https://github.com/faissaloux/termspark")],
            1: [("@faissaloux", "https://github.com/faissaloux")],
        }

    def test_reformat(self):
        position = {
            "content": [
                " By [@faissaloux](https://github.com/faissaloux) [@termspark](https://github.com/termspark) ",
                " Text ",
            ],
            "color": ["green", "red"],
            "highlight": ["", "black"],
            "style": ["", ""],
        }

        detected = Hyperlink.exists_in(position["content"])
        reformated = Hyperlink().reformat(position, detected)

        assert reformated == [
            " By ",
            "[@faissaloux](https://github.com/faissaloux)",
            " ",
            "[@termspark](https://github.com/termspark)",
            " ",
            " Text ",
        ]
        assert position == {
            "content": [
                " By ",
                "[@faissaloux](https://github.com/faissaloux)",
                " ",
                "[@termspark](https://github.com/termspark)",
                " ",
                " Text ",
            ],
            "color": ["green", "green", "green", "green", "green", "red"],
            "highlight": ["", "", "", "", "", "black"],
            "style": ["", "", "", "", "", ""],
        }

    def test_reformat_separated_hyperlinks_same_position(self):
        position = {
            "content": [
                " [@faissaloux](https://github.com/faissaloux) ",
                "[@termspark](https://github.com/faissaloux/termspark)",
            ],
            "color": ["green", "red"],
            "highlight": ["", "black"],
            "style": ["", ""],
        }

        detected = Hyperlink.exists_in(position["content"])
        reformated = Hyperlink().reformat(position, detected)

        assert reformated == [
            " ",
            "[@faissaloux](https://github.com/faissaloux)",
            " ",
            "[@termspark](https://github.com/faissaloux/termspark)",
        ]
        assert position == {
            "content": [
                " ",
                "[@faissaloux](https://github.com/faissaloux)",
                " ",
                "[@termspark](https://github.com/faissaloux/termspark)",
            ],
            "color": ["green", "green", "green", "red"],
            "highlight": ["", "", "", "black"],
            "style": ["", "", "", ""],
        }

    def test_encode_one_element(self):
        position = {
            "content": [" [@termspark](https://github.com/faissaloux/termspark) "],
            "color": ["green"],
            "highlight": [""],
            "style": [""],
        }

        hyperlink = Hyperlink()
        detected = Hyperlink.exists_in(position["content"])
        reformated = hyperlink.reformat(position, detected)
        hyperlink.set_content(reformated)
        encoded = hyperlink.encode()

        assert encoded == [
            {
                "index": 1,
                "placeholder": "@termspark",
                "hyperlink": Hyperlink.HYPERLINK_PREFIX
                + "https://github.com/faissaloux/termspark"
                + "\x1b\\"
                + "@termspark"
                + Hyperlink.HYPERLINK_SUFFIX
                + "\x1b\\",
            }
        ]

    def test_encode_multiple_elements_with_one_hyperlink(self):
        position = {
            "content": [
                "Termspark repository: ",
                " [@termspark](https://github.com/faissaloux/termspark) ",
            ],
            "color": ["green", ""],
            "highlight": ["", ""],
            "style": ["", ""],
        }

        hyperlink = Hyperlink()
        detected = Hyperlink.exists_in(position["content"])
        reformated = hyperlink.reformat(position, detected)
        hyperlink.set_content(reformated)
        encoded = hyperlink.encode()

        assert encoded == [
            {
                "index": 2,
                "placeholder": "@termspark",
                "hyperlink": Hyperlink.HYPERLINK_PREFIX
                + "https://github.com/faissaloux/termspark"
                + "\x1b\\"
                + "@termspark"
                + Hyperlink.HYPERLINK_SUFFIX
                + "\x1b\\",
            }
        ]

    def test_encode_multiple_elements_with_multiple_hyperlinks(self):
        position = {
            "content": [
                " [@termspark](https://github.com/faissaloux/termspark) ",
                "[@faissaloux](https://github.com/faissaloux)",
            ],
            "color": ["green", ""],
            "highlight": ["", ""],
            "style": ["", ""],
        }

        hyperlink = Hyperlink()
        detected = Hyperlink.exists_in(position["content"])
        reformated = hyperlink.reformat(position, detected)
        hyperlink.set_content(reformated)
        encoded = hyperlink.encode()

        assert encoded == [
            {
                "index": 1,
                "placeholder": "@termspark",
                "hyperlink": Hyperlink.HYPERLINK_PREFIX
                + "https://github.com/faissaloux/termspark"
                + "\x1b\\"
                + "@termspark"
                + Hyperlink.HYPERLINK_SUFFIX
                + "\x1b\\",
            },
            {
                "index": 3,
                "placeholder": "@faissaloux",
                "hyperlink": Hyperlink.HYPERLINK_PREFIX
                + "https://github.com/faissaloux"
                + "\x1b\\"
                + "@faissaloux"
                + Hyperlink.HYPERLINK_SUFFIX
                + "\x1b\\",
            },
        ]
