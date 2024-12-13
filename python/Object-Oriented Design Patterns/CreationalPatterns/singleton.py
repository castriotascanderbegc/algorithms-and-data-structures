"""
    Design Pattern: Singleton Pattern

    Below shows an example of the usage of Singleton Pattern in a single-threaded env
"""


class Singleton:
    _unique_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not cls._unique_instance:
            cls._unique_instance = super(Singleton, cls).__new__(cls)
            #cls._unique_instance._init_singleton()

        return cls._unique_instance


    """def _init_singleton(self):
        self.value = None"""

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
