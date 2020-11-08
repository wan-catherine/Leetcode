import bisect
import sys

"""
From this problem, I learn that we can use bisect in the list not only the single number . 
"""
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = [[-sys.maxsize, -sys.maxsize], [sys.maxsize, sys.maxsize]]

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        index = bisect.bisect(self.intervals, [val])
        ps, pe = self.intervals[index-1]
        ns, ne = self.intervals[index]
        if pe + 1 == val and val + 1 == ns:
            self.intervals = self.intervals[:index-1] + [[ps, ne]] + self.intervals[index+1:]
        elif pe + 1 == val:
            self.intervals[index-1][1] = val
        elif val + 1 == ns:
            self.intervals[index][0] = val
        elif pe + 1 < val and val + 1 < ns:
            self.intervals = self.intervals[:index] + [[val, val]] + self.intervals[index:]

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals[1:-1]