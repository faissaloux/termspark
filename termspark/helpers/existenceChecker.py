from typing import Dict

class ExistenceChecker:
    def dictionary_key(self, dictionary: Dict, key: str, default: str = '') -> str:
        return dictionary[key] if key in dictionary.keys() else default
