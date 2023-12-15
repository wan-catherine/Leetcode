from typing import List

"""
dp[i] : nums[0:i+1] all beautiful and nums[i] will be changed to equal or larger than k if necessary
"""
class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = max(0, k - nums[0])
        dp[1] = max(0, k - nums[1])
        dp[2] = max(0, k - nums[2])
        for i in range(3, length):
            dp[i] = max(0, k - nums[i]) + min(dp[i-1], dp[i-2], dp[i-3])
        return min(dp[length-3:])

