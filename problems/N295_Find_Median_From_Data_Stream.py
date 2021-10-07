import bisect
import heapq


class MedianFinder_before(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        bisect.insort_left(self.arr, num)
        self.size += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size % 2:
            return self.arr[self.size // 2]
        else:
            index = self.size // 2
            res = self.arr[self.size // 2]
            if index - 1 >= 0:
                res += self.arr[index - 1]
            return res / 2

class MedianFinder(object):
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -num)
            v = heapq.heappop(self.large)
            heapq.heappush(self.small, -v)
        else:
            heapq.heappush(self.small, num)
            v = heapq.heappop(self.small)
            heapq.heappush(self.large, -v)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (self.small[0] - self.large[0]) / 2
        return self.small[0]

