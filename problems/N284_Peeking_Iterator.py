from collections import deque


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = deque()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache:
            return self.cache[-1]
        if not self.iterator.hasNext():
            return None
        num = self.iterator.next()
        self.cache.append(num)
        return num

    def next(self):
        """
        :rtype: int
        """
        if self.cache:
            return self.cache.popleft()
        if not self.iterator.hasNext():
            return None
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cache:
            return True
        if self.iterator.hasNext():
            return True
        return False