class ExistenceChecker:
    def dictionary_key(self, dictionary, key, default = ''):
        return dictionary[key] if key in dictionary.keys() else default
