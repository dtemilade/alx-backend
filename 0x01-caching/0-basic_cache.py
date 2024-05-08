#!/usr/bin/python3
"""
    class  that inherits from BaseCaching and is a caching system:
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ class  that inherits from BaseCaching and is a caching system:
    """

    def put(self, key, item):
        """ Method to assign to the dictionary.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Method to return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key, None)
