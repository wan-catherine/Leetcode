import bisect
import sys


class Solution(object):
    def findUnsortedSubarray_bisect(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == sorted(nums):
            return 0

        res = []
        start, end = None, None
        for i, v in enumerate(nums):
            index = bisect.bisect(res, v)
            if index == len(res):
                res.append(v)
                continue
            bisect.insort(res, v)
            if start == None:
                start = index
            elif start > index:
                start = index
            end = i
        return end - start + 1

    def findUnsortedSubarray(self, nums):
        start, end = -1, -1
        stack = []
        maximum = -sys.maxsize
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] > v:
                index = stack.pop()
                maximum = max(maximum, nums[index])
                if start == -1 or start > index:
                    start = index
                end = i
            if start > -1 and v < maximum:
                end = i
            stack.append(i)
        return end - start + 1 if start > -1 and end > -1 else 0

