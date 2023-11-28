import pytest

from termspark.exceptions.maxLenNotSupported import MaxLenNotSupported
from termspark.exceptions.minNotReachedException import MinNotReachedException
from termspark.termspark import TermSpark


class TestMaxLength:
    def test_max_length_with_spark(self):
        termspark = TermSpark()
        termspark.spark_left(["LEFT", "red"])
        termspark.spark_center(["CENTER", "green"])
        termspark.spark_right(["RIGHT", "blue"])
        termspark.max_left(2)
        termspark.max_center(2)
        termspark.max_right(2)

        assert termspark.left["content"][0] == "LE"
        assert termspark.center["content"][0] == "CE"
        assert termspark.right["content"][0] == "RI"

    def test_max_length_not_supported_by_print(self):
        termspark = TermSpark()
        termspark.spark_left(["LEFT", "red"])
        termspark.print_right("RIGHT", "blue")
        termspark.max_left(2)

        with pytest.raises(MaxLenNotSupported):
            termspark.max_right(2)

    def test_max_length_with_multiple_content_first_elem_longer_than_max(self):
        termspark = TermSpark()
        termspark.spark_center([" CENTER| ", "gray", "white"])
        termspark.spark_center([" RETNER ", "white", "blue"])
        termspark.max_center(3)

        assert len(termspark.center["content"]) == 1
        assert len(termspark.center["color"]) == 1
        assert len(termspark.center["highlight"]) == 1
        assert termspark.center["content"][0] == " CE"
        assert termspark.center["color"][0] == "gray"
        assert termspark.center["highlight"][0] == "white"

    def test_max_length_with_multiple_content_first_elem_less_than_max(self):
        termspark = TermSpark()
        termspark.spark_center([" CENTER| ", "gray", "white"])
        termspark.spark_center([" RETNER ", "white", "blue"])
        termspark.max_center(11)

        assert len(termspark.center["content"]) == 2
        assert len(termspark.center["color"]) == 2
        assert len(termspark.center["highlight"]) == 2
        assert termspark.center["content"][0] == " CENTER| "
        assert termspark.center["content"][1] == " R"
        assert termspark.center["color"][0] == "gray"
        assert termspark.center["color"][1] == "white"
        assert termspark.center["highlight"][0] == "white"
        assert termspark.center["highlight"][1] == "blue"

    def test_max_length_with_single_content_first_elem_equal_to_max(self):
        termspark = TermSpark()
        termspark.spark_center([" CENTER ", "gray", "white"])
        termspark.max_center(8)

        assert len(termspark.center["content"]) == 1
        assert len(termspark.center["color"]) == 1
        assert len(termspark.center["highlight"]) == 1
        assert termspark.center["content"][0] == " CENTER "
        assert termspark.center["color"][0] == "gray"
        assert termspark.center["highlight"][0] == "white"

    def test_max_length_with_multiple_content_first_elem_equal_to_max(self):
        termspark = TermSpark()
        termspark.spark_center([" CENTER| ", "gray", "white"])
        termspark.spark_center([" RETNER ", "white", "blue"])
        termspark.max_center(9)

        assert len(termspark.center["content"]) == 1
        assert len(termspark.center["color"]) == 1
        assert len(termspark.center["highlight"]) == 1
        assert termspark.center["content"][0] == " CENTER| "
        assert termspark.center["color"][0] == "gray"
        assert termspark.center["highlight"][0] == "white"

    def test_max_length_minimum_value(self):
        termspark = TermSpark()
        termspark.spark_center([" CENTER ", "gray", "white"])

        with pytest.raises(MinNotReachedException):
            termspark.max_center(0)
