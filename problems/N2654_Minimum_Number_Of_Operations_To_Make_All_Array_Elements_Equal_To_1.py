import math
import sys
from typing import List

"""
If 1 in the nums, then length - count(1)
if not : 
we need to get the shortest subarray which gcd is 1. 
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        if 1 in nums:
            ones = 0
            for n in nums:
                if n == 1:
                    ones += 1
            return length - ones

        diff = sys.maxsize
        for i in range(length - 1):
            cur = nums[i]
            for j in range(i+1, length):
                cur = math.gcd(cur, nums[j])
                if cur == 1:
                    diff = min(diff, j - i)
        if diff == sys.maxsize:
            return -1
        return diff + length - 1
