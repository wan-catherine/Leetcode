# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert_before(self, intervals, newInterval):
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

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        l, r = newInterval
        s, e = newInterval
        for i, li in enumerate(intervals):
            if l > li[1]:
                continue
            s = l if l < li[0] else li[0]
            break
        for j, li in enumerate(intervals[::-1]):
            if li[0] > r:
                continue
            e = li[1] if r <= li[1] else r
            break
        if [s, e] not in intervals:
            intervals.append([s, e])
        for i, j in intervals:
            if j < s:
                res.append([i, j])
            elif i > e:
                res.append([i, j])
            elif i == s and j == e:
                res.append([i, j])
        return sorted(res, key=lambda li: li[0])
