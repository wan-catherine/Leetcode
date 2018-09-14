# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        startInter = {}
        for i in intervals:
            if i.start not in startInter:
                startInter[i.start] = i
            elif i.end > startInter[i.start].end:
                startInter[i.start] = i

        sortedStarts = sorted(startInter)
        first = startInter[sortedStarts[0]]
        res = []

        if len(sortedStarts) < 2:
            return [first]

        for i in range(1,len(sortedStarts)):
            if startInter[sortedStarts[i]].start > first.end:
                res.append(first)
                first = startInter[sortedStarts[i]]
            elif first.end < startInter[sortedStarts[i]].end:
                first = Interval(first.start, startInter[sortedStarts[i]].end)
            if i == len(sortedStarts) - 1:
                res.append(first)
        return res


