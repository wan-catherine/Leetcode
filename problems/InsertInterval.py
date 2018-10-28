# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == None or len(intervals) == 0:
            return [newInterval]
        res = []

        i = 0
        while i < len(intervals):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i += 1
                continue
            if intervals[i].start > newInterval.end:
                res.append(newInterval)
                break

            newInterval.start = intervals[i].start if intervals[i].start < newInterval.start else newInterval.start
            newInterval.end = intervals[i].end if intervals[i].end > newInterval.end else newInterval.end
            i += 1
        if i < len(intervals):
            res.extend(intervals[i:])
        else:
            res.append(newInterval)
        return res