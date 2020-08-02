import bisect


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            bisect.insort(self.array, key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        index = bisect.bisect_left(self.array, key)
        del self.array[index]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.array

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(100)
print(obj.contains(2))
print(obj.contains(100))
obj.remove(1)
print(obj.contains(1))
