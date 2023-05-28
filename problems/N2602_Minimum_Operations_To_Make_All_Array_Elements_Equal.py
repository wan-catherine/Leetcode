import bisect
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        length = len(nums)
        prev, suff = nums[:], nums[:]
        for i in range(1, length):
            prev[i] += prev[i-1]
        for i in range(length-2, -1, -1):
            suff[i] += suff[i+1]

        res = []
        for que in queries:
            idx = bisect.bisect_left(nums, que)
            left, right = 0, 0
            if idx == length:
                left += que * length - prev[-1]
            elif idx == 0:
                right += suff[0] - que * length
            else:
                left += que * idx - prev[idx - 1]
                right += suff[idx] - que * (length - idx)
            res.append(left + right)
        return res
