import math
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        length = len(nums)
        res = 0

        for i in range(1, length + 1):
            cur = 0
            j = 1
            while True:
                idx = j * j * i
                if idx > length:
                    break
                cur += nums[idx - 1]
                j += 1
            res = max(res, cur)
        return res



