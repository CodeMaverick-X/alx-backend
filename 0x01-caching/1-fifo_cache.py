#!/usr/bin/env python3
"""
conatins a class FIFOCache that inherits
from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """implements fifo caching technique
    """

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """asigns to dict self.cache_data
        the item value for the key `key`
        """
        if len(self.cache_data) >= self.MAX_ITEMS\
           and key not in self.cache_data.keys():
            f_key = list(self.cache_data.keys())[0]
            del self.cache_data[f_key]
            print('DISCARD: {}'.format(f_key))

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get cache val"""
        if key:
            return self.cache_data.get(key)
        return None
