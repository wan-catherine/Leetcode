from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        length = len(types)
        dp = [[0] * (target + 1) for _ in range(length + 1)]

        dp[0][0] = 1

        for i in range(length):
            for j in range(target + 1):
                m, c = types[i]
                k = 0
                while k <= m and k * c <= j:
                    dp[i+1][j] += dp[i][j - k * c] % MOD
                    k += 1

        # for li in dp:
        #     print(li)
        return dp[length][target] % MOD
