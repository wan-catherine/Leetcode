import math
from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        length = len(nums)
        res = 0
        for i in range(length):
            v = nums[i]
            for j in range(i, length):
                v = lcm(v, nums[j])
                if v == k:
                    res += 1
        return res