import math
from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        m = 10 ** 9 + 7
        length = len(requirements)
        for i in range(length):
            requirements[i][0] += 1
        requirements.sort()

        dp = [[0 for _ in range(405)] for _ in range(305)]
        dp[0][0] = 1

        cur, limit = 0, 0
        icur = 0
        for i in range(1, n + 1):
            if i == requirements[icur][0]:
                cur = requirements[icur][1]
                limit = cur
                icur += 1
            else:
                limit = requirements[icur][1]

            for j in range(cur, limit + 1):
                for k in range(j+1):
                    if j - k <= i - 1:
                        dp[i][j] += dp[i-1][k]
                        dp[i][j] %= m
            if icur == length:
                res = dp[i][cur]
                return res * math.perm(n - i) % m


