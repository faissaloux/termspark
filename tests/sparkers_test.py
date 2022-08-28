from termspark import TermSpark

class TestSparkers:
    def test_can_set_left_content(self):
        termspark = TermSpark()

        termspark.spark_left('LEFT')
        assert termspark.left['content'] == ['LEFT']

    def test_can_set_left_color(self):
        termspark = TermSpark()

        termspark.spark_left('LEFT', 'white')
        assert termspark.left['content'] == ['LEFT']
        assert termspark.left['color'] == ['white']

    def test_can_set_left_highlight(self):
        termspark = TermSpark()

        termspark.spark_left('LEFT', 'white', 'red')
        assert termspark.left['content'] == ['LEFT']
        assert termspark.left['color'] == ['white']
        assert termspark.left['highlight'] == ['red']

    def test_can_set_right_content(self):
        termspark = TermSpark()

        termspark.spark_right('RIGHT')
        assert termspark.right['content'] == ['RIGHT']

    def test_can_set_right_color(self):
        termspark = TermSpark()

        termspark.spark_right('RIGHT', 'white')
        assert termspark.right['content'] == ['RIGHT']
        assert termspark.right['color'] == ['white']

    def test_can_set_right_highlight(self):
        termspark = TermSpark()

        termspark.spark_right('RIGHT', 'white', 'blue')
        assert termspark.right['content'] == ['RIGHT']
        assert termspark.right['color'] == ['white']
        assert termspark.right['highlight'] == ['blue']

    def test_can_set_center_content(self):
        termspark = TermSpark()

        termspark.spark_center('CENTER')
        assert termspark.center['content'] == ['CENTER']

    def test_can_set_center_color(self):
        termspark = TermSpark()

        termspark.spark_center('CENTER', 'white')
        assert termspark.center['content'] == ['CENTER']
        assert termspark.center['color'] == ['white']

    def test_can_set_center_highlight(self):
        termspark = TermSpark()

        termspark.spark_center('CENTER', 'white', 'green')
        assert termspark.center['content'] == ['CENTER']
        assert termspark.center['color'] == ['white']
        assert termspark.center['highlight'] == ['green']

    def test_can_set_multiple_same_position_content(self):
        termspark = TermSpark()

        termspark.spark_right([' * ', 'black', 'gray'], [' RIGHT ', 'white', 'blue'])
        termspark.spark_left([' * ', 'black', 'gray'], [' LEFT ', 'white', 'red'])

        assert termspark.right['content'] == [' * ', ' RIGHT ']
        assert termspark.right['color'] == ['black', 'white']
        assert termspark.right['highlight'] == ['gray', 'blue']

        assert termspark.left['content'] == [' * ', ' LEFT ']
        assert termspark.left['color'] == ['black', 'white']
        assert termspark.left['highlight'] == ['gray', 'red']

    def test_can_append_same_position_content_by_separate_sparkers(self):
        termspark = TermSpark()

        termspark.spark_right([' * ', 'black', 'gray'])
        termspark.spark_right([' RIGHT ', 'white', 'blue'])
        termspark.spark_left([' * ', 'black', 'gray'])
        termspark.spark_left([' LEFT ', 'white', 'red'])

        assert termspark.right['content'] == [' * ', ' RIGHT ']
        assert termspark.right['color'] == ['black', 'white']
        assert termspark.right['highlight'] == ['gray', 'blue']

        assert termspark.left['content'] == [' * ', ' LEFT ']
        assert termspark.left['color'] == ['black', 'white']
        assert termspark.left['highlight'] == ['gray', 'red']