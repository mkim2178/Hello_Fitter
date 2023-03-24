
"""
The Storage class represents the storage of shaft or grip!
"""


class Storage:

    def __init__(self, name, storage):
        """
        This is an init method (constructor that initializes the Storage object).
        It includes the name of the storage and a dictionary (keys: name of the shaft/grip, values: the amount of shafts/grips left).

        :param str name: name of the storage (will be 'Shaft Storage' or 'Grip Storage')
        :param dict storage: a dictionary that shows how many certain shaft/grip left (ex: {"Diamana": 5} -> this means the 'Shaft Storage' has 5 'Diamana' shafts left).
        """

        self.name = name
        self.storage = storage


    def take_item(self, name):
        """
        This method decrement 1 from a value that is located in self.storage[name].

        :param str name: the name of shaft/grip.
        :return: None
        """

        self.storage[name] -= 1


    def __repr__(self):
        """
        This is a repr method; an object representation of the 'Storage' object (the format is formal).

        :return: a string that represents the 'Storage' object (ex: Storage(Shaft Storage, {'Diamana': 5, 'Tensei': 10})).
        """

        return f"Storage({self.name}, {self.storage})"


    def __str__(self):
        """
        This is a str method; also an object representation of the 'Storage' object, but it is legible for human (informal).
        It includes repr() built-in function to include the quotes.

        If you only put self.name, it will give >>> Shaft Storage
        However, if you put repr(self.name), this will give >>> 'Shaft Storage'

        :return: a string that represents the 'Storage' object (ex: "Name: 'Shaft Storage' / Storage Status: {'Diamana': 5, 'Tensei': 10}")
        """

        return f"Name: {repr(self.name)} / Storage Status: {self.storage}"

