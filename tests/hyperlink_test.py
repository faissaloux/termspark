from termspark.hyperlink.hyperlink import Hyperlink


class TestHyperlink:
    def test_attributes(self):
        assert (
            Hyperlink.HYPERLINK_PATTERN
            == "\\[([^\\[]*?)]\\(\\s*(http[s]?://[^)]+)\\s*\\)"
        )
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

    def test_encode_one_element(self):
        content = [" [@termspark](https://github.com/faissaloux/termspark) "]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)
        hyperlink.exists()
        encoded = hyperlink.encode()

        assert encoded == [
            [
                {
                    "@termspark": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux/termspark"
                    + "\x1b\\"
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                }
            ]
        ]

    def test_encode_multiple_elements_with_one_hyperlink(self):
        content = [
            "Termspark repository: ",
            " [@termspark](https://github.com/faissaloux/termspark) ",
        ]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)
        hyperlink.exists()
        encoded = hyperlink.encode()

        assert encoded == [
            [],
            [
                {
                    "@termspark": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux/termspark"
                    + "\x1b\\"
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                }
            ],
        ]

    def test_encode_multiple_elements_with_multiple_hyperlinks(self):
        content = [
            " [@termspark](https://github.com/faissaloux/termspark) ",
            "[@faissaloux](https://github.com/faissaloux)",
        ]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)
        hyperlink.exists()
        encoded = hyperlink.encode()

        assert encoded == [
            [
                {
                    "@termspark": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux/termspark"
                    + "\x1b\\"
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                }
            ],
            [
                {
                    "@faissaloux": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux"
                    + "\x1b\\"
                    + "@faissaloux"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                }
            ],
        ]

    def test_encode_multiple_elements_with_multiple_hyperlinks_in_the_same_element(
        self,
    ):
        content = [
            " [@termspark](https://github.com/faissaloux/termspark)",
            "[@github](https://github.com/faissaloux) [@twitter](https://twitter.com/faissaloux)",
        ]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)
        hyperlink.exists()
        encoded = hyperlink.encode()

        assert encoded == [
            [
                {
                    "@termspark": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux/termspark"
                    + "\x1b\\"
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                }
            ],
            [
                {
                    "@github": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux"
                    + "\x1b\\"
                    + "@github"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                },
                {
                    "@twitter": Hyperlink.HYPERLINK_PREFIX
                    + "https://twitter.com/faissaloux"
                    + "\x1b\\"
                    + "@twitter"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + "\x1b\\"
                },
            ],
        ]
