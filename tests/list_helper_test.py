from termspark.helpers.list import List

class TestListHelper:
    def test_mono_word_list_to_snake(self):
        assert List().snake(['red']) == ['red']

    def test_multi_word_list_to_snake(self):
        assert List().snake(['red', 'light red']) == ['red', 'light_red']

    def test_none_to_snake(self):
        assert List().snake([None, 'light blue']) == [None, 'light_blue']