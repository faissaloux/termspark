from termspark.hyperlink.hyperlink import Hyperlink


class TestHyperlink:
    def test_attributes(self):
        assert (
            Hyperlink.HYPERLINK_PATTERN
            == "\\[([^\\[]*?)]\\(\\s*(http[s]?://[^)]+)\\s*\\)"
        )
        assert Hyperlink.HYPERLINK_PREFIX == "\x1b]8;;"
        assert Hyperlink.HYPERLINK_SUFFIX == "\x1b]8;;"
        assert Hyperlink.RESET == "\x1b\\"

    def test_set_content(self):
        content = [" Link ", "[@faissaloux](https://github.com/faissaloux)"]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)

        assert hyperlink.content == content

    def test_exists_no_hyperlink(self):
        content = [" Link "]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)

        assert hyperlink.exists() == False

    def test_exists_one_hyperlink(self):
        content = [" Link ", "[@faissaloux](https://github.com/faissaloux)"]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)

        assert hyperlink.exists() == True

    def test_exists_multiple_hyperlinks(self):
        content = [
            " [@termspark](https://github.com/faissaloux/termspark) ",
            "[@faissaloux](https://github.com/faissaloux)",
        ]
        hyperlink = Hyperlink()
        hyperlink.set_content(content)

        assert hyperlink.exists() == True

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
                    + Hyperlink.RESET
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
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
            "Termspark repository: ",
            [
                {
                    "@termspark": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux/termspark"
                    + Hyperlink.RESET
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
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
                    + Hyperlink.RESET
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
                }
            ],
            [
                {
                    "@faissaloux": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux"
                    + Hyperlink.RESET
                    + "@faissaloux"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
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
                    + Hyperlink.RESET
                    + "@termspark"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
                }
            ],
            [
                {
                    "@github": Hyperlink.HYPERLINK_PREFIX
                    + "https://github.com/faissaloux"
                    + Hyperlink.RESET
                    + "@github"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
                },
                {
                    "@twitter": Hyperlink.HYPERLINK_PREFIX
                    + "https://twitter.com/faissaloux"
                    + Hyperlink.RESET
                    + "@twitter"
                    + Hyperlink.HYPERLINK_SUFFIX
                    + Hyperlink.RESET
                },
            ],
        ]
