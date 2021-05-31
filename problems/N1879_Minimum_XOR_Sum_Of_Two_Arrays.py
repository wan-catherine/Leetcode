import sys
from typing import List


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        dp = [sys.maxsize] * (1 << length)
        dp[0] = 0
        for status in range(1, 2 ** length):
            ones = bin(status).count('1') - 1
            for i in range(length):
                if status & (1 << i):
                    dp[status] = min(dp[status], dp[status - (1 << i)] + (nums1[ones] ^ nums2[i]))
        return dp[-1]