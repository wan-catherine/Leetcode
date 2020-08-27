import collections


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        if not intervals:
            return []
        self.length = len(intervals)
        if self.length == 1:
            return [-1]
        for index, li in enumerate(intervals):
            li.append(index)

        intervals.sort(key=lambda li:li[0])
        memo = collections.defaultdict(int) # end:index
        res = [-1]*self.length
        self.intervals = intervals
        for i,j,k in intervals:
            if j in memo:
                res[k] = memo[j]
            else:
                res[k] = self.bs(j)
                memo[j] = res[k]
        return res

    def bs(self, target):
        left, right = 0, self.length
        while left < right:
            mid = (right - left) // 2 + left
            if self.intervals[mid][0] == target:
                return self.intervals[mid][2]
            if self.intervals[mid][0] > target:
                right = mid
            else:
                left = mid + 1
        if left == self.length:
            return -1
        return self.intervals[left][2]

