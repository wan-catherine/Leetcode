from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        nums.insert(0, 0)
        MOD = 10 ** 9 + 7
        length = len(nums)
        dp = [[0] * k for _ in range(length)]
        dp[0][0] = 1
        for i in range(1, length):
            for j in range(0, k):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] += dp[i-1][j-nums[i]]
                dp[i][j] %= MOD
        total = 2 ** (length - 1) % MOD
        invalid = 0
        for i in range(k):
            invalid += dp[length-1][i]
            invalid %= MOD

        return (total - 2 * invalid) % MOD

