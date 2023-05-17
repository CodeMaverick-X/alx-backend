#!/usr/bin/env python3
"""
contains class BasicCache that inherits from
BasicCacheing and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class that extends the base_caching class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """asings to dict self.cache_data the item
        value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """must return a value in the self.cache_data
        linked to key"""
        if key:
            return self.cache_data.get(key)
        return None
