"""OrderedDict in such a way that the order shows how recently they were used. In the beginning, we will have least
recently used and in the end, most recently used. If any update OR query is made to a key it moves to the end (most
recently used). If anything is added, it is added at the end (most recently used/added) For get(key): we return the
value of the key that is queried in O(1) and return -1 if we don’t find the key in out dict/cache. And also move the
key to the end to show that it was recently used. For put(key, value): first, we add/ update the key by conventional
methods. And also move the key to the end to show that it was recently used. But here we will also check whether the
length of our ordered dictionary has exceeded our capacity, If so we remove the first key (least recently used)
Time complexity is O(1)
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]


cache = LRUCache(2)
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)
