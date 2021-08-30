import collections
from collections import OrderedDict
"""
Hashtable and DoubleList
dictionary<key, node>
node: 
    val, 
    prev,
    next
"""

class LRUCache_orderedDict(object):

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

"""
We need ot maintain an order which the latest one is the at end . 
But move an element in an array will be o(n), so we can consider double-linklist . 
Use a dict to record all key-node.
"""
class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.kv = collections.defaultdict(Node)
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val

    def remove_node(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def add_node(self, node):
        prev = self.tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            node = self.kv[key]
            self.remove_node(node)
        elif len(self.kv) == self.capacity:
            del self.kv[self.head.nxt.key]
            self.remove_node(self.head.nxt)
        node = Node(key, value)
        self.kv[key] = node
        self.add_node(node)
