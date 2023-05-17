#!/usr/bin/env python3
"""
implements the MRU caceh algo
in the class MRUCache
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """class that implements the MRU algo
    """

    count = 0
    switch = 0

    def __init__(self):
        """init"""
        super().__init__()
        self.cache_age = {}

    def put(self, key, item):
        """cache value with key"""
        if len(self.cache_age) > 1:
            MRUCache.switch = 1
        else:
            MRUCache.switch = 0
        self.cache_age[key] = MRUCache.count = MRUCache.count + 1
        if MRUCache.switch:
            max_v = max(list(self.cache_age.values())[:-1])
        else:
            max_v = max(list(self.cache_age.values()))

        mru_key = [k for k, v in self.cache_age.items() if v == max_v][0]

        if len(self.cache_data) >= self.MAX_ITEMS\
           and key not in self.cache_data.keys():
            del self.cache_data[mru_key]
            del self.cache_age[mru_key]
            print('DISCARD: {}'.format(mru_key))
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get val from cache """
        if key:
            if key in self.cache_data.keys():
                self.cache_age[key] = MRUCache.count = MRUCache.count + 1
            return self.cache_data.get(key)
        return None
