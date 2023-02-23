from termspark.helpers.existenceChecker import ExistenceChecker


class TestExistenceChecker:
    def test_dictionary_not_existed_key_default(self):
        dictionary = {}

        assert ExistenceChecker().dictionary_key(dictionary, "key") == ""

    def test_dictionary_not_existed_can_set_default_key(self):
        dictionary = {}

        assert (
            ExistenceChecker().dictionary_key(dictionary, "key", "default") == "default"
        )

    def test_dictionary_existed_key(self):
        dictionary = {
            "key": "value",
        }

        assert ExistenceChecker().dictionary_key(dictionary, "key") == "value"
