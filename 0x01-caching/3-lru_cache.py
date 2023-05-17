#!/usr/bin/env python3
"""
implements the LRU caceh algo
in the class LRUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class that implements the LRU algo
    """

    count = 0

    def __init__(self):
        """init"""
        super().__init__()
        self.cache_age = {}

    def put(self, key, item):
        self.cache_age[key] = LRUCache.count = LRUCache.count + 1
        min_v = min(list(self.cache_age.values()))

        lru_key = [k for k, v in self.cache_age.items() if v == min_v][0]

        if len(self.cache_data) >= self.MAX_ITEMS\
           and key not in self.cache_data.keys():
            del self.cache_data[lru_key]
            del self.cache_age[lru_key]
            print('DISCARD: {}'.format(lru_key))
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get val from cache """
        if key:
            if key in self.cache_data.keys():
                self.cache_age[key] = LRUCache.count = LRUCache.count + 1
            return self.cache_data.get(key)
        return None
