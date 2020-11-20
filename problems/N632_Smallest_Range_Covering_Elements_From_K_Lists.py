import bisect
from collections import deque


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        length = len(nums)
        arr = sorted([(li[0], i) for i, li in enumerate(nums)])
        lens = [len(li) for li in nums]
        indexes = [0] * length
        res = [arr[0][0], arr[-1][0]]
        while True:
            idx = 0
            while indexes[arr[idx][1]] == lens[arr[idx][1]] - 1:
                idx += 1
                if idx == length:
                    return res
            val, i = arr[idx]
            arr = arr[:idx] + arr[idx+1:]
            indexes[i] += 1
            bisect.insort_left(arr, (nums[i][indexes[i]], i))
            if arr[-1][0] - arr[0][0] < res[1] - res[0]:
                res = [arr[0][0], arr[-1][0]]

