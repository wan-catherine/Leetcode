import bisect


class MedianFinder(object):

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
