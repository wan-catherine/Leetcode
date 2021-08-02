import bisect
import sys
from typing import List


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

    """
    update : 202100802
    steps: 
        1. from left to right, find the first left index which a > b 
        2. from right to left, find the first right index which a > b
        3. find the maximum and minimum in range [start, end] (both included)
        4. extend to left if there is any num > minimum of #3
        5. extend to right if there is any num < maximum of #3
    """
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        start = end = 0
        for i in range(1, length):
            if nums[i] >= nums[i - 1]:
                continue
            start = i - 1
            break
        for i in range(length - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            end = i + 1
            break
        m, n = -sys.maxsize, sys.maxsize
        for i in range(start, end + 1):
            m = max(m, nums[i])
            n = min(n, nums[i])
        while start - 1 >= 0:
            if nums[start - 1] > n:
                start -= 1
            else:
                break
        while end + 1 < length:
            if nums[end + 1] < m:
                end += 1
            else:
                break
        return end - start + 1 if end > start else 0

