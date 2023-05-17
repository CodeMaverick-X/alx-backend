#!/usr/bin/env python3
"""
contains a class that implemnets the
LIFO Caching algorithm
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """the class i wrote about in the modile doc"""
    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache"""
        if len(self.cache_data) >= self.MAX_ITEMS\
           and key not in self.cache_data.keys():
            f_key = list(self.cache_data.keys())[-1]
            del self.cache_data[f_key]
            print('DISCARD: {}'.format(f_key))

        if key in self.cache_data.keys():
            del self.cache_data[key]
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets item from cache"""
        if key:
            return self.cache_data.get(key)
        return None
