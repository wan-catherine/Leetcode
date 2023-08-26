from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        length = len(nums)
        prex = [0]
        for i in range(length):
            prex.append(nums[i] + prex[-1])
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
            if i + 1 < length:
                dp[i][i+1] = True

        for l in range(2, length):
            for i in range(length - l):
                dp[i][i + l] = dp[i][i + l - 1] and (True if prex[i+l] - prex[i] >= m else False)
                dp[i][i + l] = dp[i][i + l]  or (dp[i+1][i+l] and (True if prex[i+l+1] - prex[i+1] >= m else False))

        return dp[0][length-1]
