import sys
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        length = len(jobDifficulty)
        if length < d:
            return -1
        if length == d:
            return sum(jobDifficulty)
        dp = [[sys.maxsize] * (length) for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, length):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(1, length):
                cur = jobDifficulty[j]
                for k in range(j-1, max(i-1, 0) - 1, -1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + cur)
                    cur = max(cur, jobDifficulty[k])
        return dp[-1][-1]


