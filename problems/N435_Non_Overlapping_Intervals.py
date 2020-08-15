class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda li: (li[0], abs(li[1])))
        length = len(intervals)
        li = [intervals[0]]
        for i in range(1, length):
            if intervals[i][0] >= li[-1][1]:
                li.append(intervals[i])
            else:
                if intervals[i][1] < li[-1][1]:
                    li.pop()
                    li.append(intervals[i])

        return length - len(li)


