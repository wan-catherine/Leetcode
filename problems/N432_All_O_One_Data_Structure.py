import collections
"""
Double linklist
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
        self.keys = set()

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key2val = collections.defaultdict(int)
        self.root = ListNode(0)
        self.tail = ListNode('tail')
        self.root.next = self.tail
        self.tail.previous = self.root
        self.val2Node = collections.defaultdict(ListNode)
        self.val2Node[0]=self.root

    def remove_node(self, node):
        prev, next = node.previous, node.next
        next.previous = prev
        prev.next = next
        del self.val2Node[node.val]

    def add_node(self, prev, next, node):
        node.next = next
        next.previous = node
        prev.next = node
        node.previous = prev
        self.val2Node[node.val] = node

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.key2val:
            val = 1
            if val not in self.val2Node:
                node = ListNode(val)
                node.keys.add(key)
                self.add_node(self.root, self.root.next, node)
            else:
                self.val2Node[val].keys.add(key)
            self.key2val[key] = val
        else:
            old_val = self.key2val[key]
            val = old_val + 1
            node = self.val2Node[old_val]
            prev, next = node.previous, node.next
            if len(node.keys) == 1:
                self.remove_node(node)
            else:
                if key in node.keys:
                    node.keys.remove(key)
                prev = node

            if val not in self.val2Node:
                new_node = ListNode(val)
                new_node.keys.add(key)
                self.add_node(prev, next, new_node)
            else:
                new_node = self.val2Node[val]
                new_node.keys.add(key)
            self.key2val[key] = val

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        val = self.key2val[key]
        if not val:
            return
        node = self.val2Node[val]
        new_val = val - 1
        prev, next = node.previous, node.next
        if len(node.keys) == 1:
            self.remove_node(node)
        else:
            node.keys.remove(key)
            next = node
        if new_val not in self.val2Node:
            new_node = ListNode(new_val)
            new_node.keys.add(key)
            self.add_node(prev, next, new_node)
        elif new_val:
            new_node = self.val2Node[new_val]
            new_node.keys.add(key)
        self.key2val[key] = new_val

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.root.next == self.tail:
            return ""
        val = self.tail.previous.val
        key = self.val2Node[val].keys.pop()
        self.val2Node[val].keys.add(key)
        return key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.root.next == self.tail:
            return ""
        val = self.root.next.val
        key = self.val2Node[val].keys.pop()
        self.val2Node[val].keys.add(key)
        return key

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.inc("c")
obj.inc("c")
obj.dec("b")
obj.dec("b")
param_4 = obj.getMinKey()
print(param_4)
obj.dec("a")
param_3 = obj.getMaxKey()
print(param_3)
param_4 = obj.getMinKey()
print(param_4)
#
# obj = AllOne()
# obj.inc("hello")
# obj.inc("goodbye")
# obj.inc("hello")
# obj.inc("hello")
# param_3 = obj.getMaxKey()
# print(param_3)
# obj.inc("leet")
# obj.inc("code")
# obj.inc("leet")
# obj.dec("hello")
# obj.inc("leet")
# obj.inc("code")
# obj.inc("code")
# param_3 = obj.getMaxKey()
# print(param_3)

