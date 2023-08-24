import bisect
import sys
from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        length = len(nums)
        def helper(arr):
            res = sys.maxsize
            li = []
            for i in range(x, length):
                bisect.insort_left(li, arr[i-x])
                idx = bisect.bisect_left(li, arr[i])
                if idx < len(li):
                    res = min(res, abs(arr[i] - li[idx]))
                if idx > 0:
                    res = min(res, abs(arr[i] - li[idx-1]))
                if idx < len(li) - 1:
                    res = min(res, abs(arr[i] - li[idx+1]))
            return res
        return min(helper(nums), helper(nums[::-1]))