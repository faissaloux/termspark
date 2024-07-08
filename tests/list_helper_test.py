from termspark.helpers.list import List


class TestListHelper:
    def test_mono_word_list_to_snake(self):
        assert List().snake(["red"]) == ["red"]

    def test_multi_word_list_to_snake(self):
        assert List().snake(["red", "light red"]) == ["red", "light_red"]

    def test_none_to_snake(self):
        assert List().snake([None, "light blue"]) == [None, "light_blue"]

    def test_list_has_rgb_to_snake(self):
        assert List().snake([None, "light blue", "36,114,200"]) == [
            None,
            "light_blue",
            "36,114,200",
        ]

    def test_list_has_tuple_rgb_to_snake(self):
        assert List().snake([None, "light blue", (36, 114, 200)]) == [
            None,
            "light_blue",
            (36, 114, 200),
        ]
