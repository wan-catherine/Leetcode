class Solution(object):
    def removeCoveredIntervals_slow(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        length = len(intervals)
        res = length
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    res -= 1
                    break
        return res

    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda li:(li[0], -li[1]))
        count = 0
        c, d = intervals[0]
        for a, b in intervals[1:]:
            if c <= a and b <= d:
                count += 1
            else:
                c, d = a, b
        return len(intervals) - count
