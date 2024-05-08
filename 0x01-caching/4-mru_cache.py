#!/usr/bin/python3
""" class MRUCache that inherits from BaseCaching and is a caching system:
"""

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ 
        class that inherits from BaseCaching and is a caching system:
    """

    def __init__(self):
        """ Init
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """ Method to assign to the dictionary.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.cache_full():
                self.discard_item()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Method to return the value in self.cache_data linked to key.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)

    def cache_full(self):
        """ Method that shows self.cache_data is higher
        """
        return len(self.cache_data) >= self.MAX_ITEMS

    def discard_item(self):
        """ Method that print DISCARD
        """
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
