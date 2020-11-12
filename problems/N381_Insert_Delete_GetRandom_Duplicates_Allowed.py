import collections
import random
"""
For list, we can :
    1. insert : use append, so O(1)
    2. getRandom : we can directly choose an index , then get the value , also O(1)
    3. remove : if we use list , then it will be O(N). But we can pop the last number in O(1). 
                This way ,we can maintain a dictionary which key : num value : index of the arr . 
                Then each time, we can exchange the last and index number of arr, then pop the last . 
                So remove can be O(1)
"""

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.val_index = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        res = True
        if val in self.val_index:
            res = False
        self.arr.append(val)
        self.val_index[val].add(len(self.arr) - 1)
        return res

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_index or len(self.val_index[val]) == 0:
            return False
        tail = self.arr[-1]

        self.val_index[tail].remove(len(self.arr) - 1)
        if tail != val:
            index = self.val_index[val].pop()
            self.arr[index] = tail
            self.val_index[tail].add(index)
        self.arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = random.randint(0, len(self.arr)-1)
        return self.arr[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()