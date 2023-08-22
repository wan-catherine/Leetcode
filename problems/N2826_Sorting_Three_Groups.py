from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = sorted(nums)
        if arr == nums:
            return 0
        length = len(nums)
        dp = [[0] * 4 for _ in range(length + 2)]

        for i in range(1, length+1):
            dp[i+1][1] = dp[i][1] + (0 if nums[i-1] == 1 else 1)
            dp[i+1][2] = min(dp[i][1], dp[i][2]) + (0 if nums[i-1] == 2 else 1)
            dp[i+1][3] = min(dp[i][1], dp[i][2], dp[i][3]) + (0 if nums[i-1] == 3 else 1)

        return min(dp[-1][1:])


