import collections


class Node:
    def __init__(self, key, value, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = collections.defaultdict(Node)
        self.fre2head = collections.defaultdict(Node)
        self.fre2tail = collections.defaultdict(Node)
        self.key2fre = collections.defaultdict(int)
        self.minifre = 0
        self.fre2count = collections.defaultdict(int)

    def add_node(self, tail, node):
        prev = tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = tail
        tail.prev = node

    def remove_node(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        self.remove_node(node)
        self.fre2count[self.key2fre[key]] -= 1
        self.fre2count[self.key2fre[key] + 1] += 1
        if self.key2fre[key] + 1 not in self.fre2tail:
            head, tail = Node(0, 0), Node(0,0)
            head.nxt = tail
            tail.prev = head
            self.fre2tail[self.key2fre[key] + 1] = tail
            self.fre2head[self.key2fre[key] + 1] = head
        else:
            tail = self.fre2tail[self.key2fre[key] + 1]
        self.add_node(tail, node)
        if self.minifre == self.key2fre[key] and self.fre2count[self.key2fre[key]] == 0:
            del self.fre2head[self.key2fre[key]]
            del self.fre2tail[self.key2fre[key]]
            self.minifre += 1
        self.key2fre[key] += 1
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.key2node[key].value = value
            return
        if self.capacity == 0:
            return
        if len(self.key2node) >= self.capacity:
            head = self.fre2head[self.minifre]
            tail = self.fre2tail[self.minifre]
            if head.nxt != tail:
                del self.key2node[head.nxt.key]
                del self.key2fre[head.nxt.key]
                self.remove_node(head.nxt)
                self.fre2count[self.minifre] -= 1

        if 1 in self.fre2head:
            tail = self.fre2tail[1]
        else:
            head, tail = Node(0, 0), Node(0, 0)
            head.nxt = tail
            tail.prev = head
            self.fre2head[1] = head
            self.fre2tail[1] = tail
        self.fre2count[1] += 1
        node = Node(key, value)
        self.key2node[key] = node
        self.add_node(tail, node)
        self.key2fre[key] = 1
        self.minifre = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(3)
# obj.put(2,2)
# obj.put(1,1)
# print(obj.get(2))
# print(obj.get(1))
# print(obj.get(2))
# obj.put(3,3)
# obj.put(4,4)
# print(obj.get(3))
# print(obj.get(2))
# print(obj.get(1))
# print(obj.get(4))


obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
print(obj.get(3))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))