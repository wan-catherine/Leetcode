from collections import OrderedDict
"""
Hashtable and DoubleList
dictionary<key, node>
node: 
    val, 
    prev,
    next
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value
