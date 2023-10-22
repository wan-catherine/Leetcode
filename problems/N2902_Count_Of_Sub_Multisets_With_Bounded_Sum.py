import collections
from typing import List


class Solution:
    def countSubMulttisets(self, nums: List[int], l: int, r: int) -> int:
        zero, group = 0, collections.defaultdict(int)
        MOD = 10 ** 9 + 7
        for n in nums:
            if n == 0:
                zero += 1
            else:
                group[n] += 1

        garr = [(0,0)]
        for n, c in group.items():
            garr.append((n, c))
        lg = len(garr)
        def helper(limit):
            if limit < 0:
                return 0
            dp = [[0] * (limit + 1) for _ in range(lg)]
            dp[0][0] = 1
            for i in range(1, lg):
                v, c = garr[i]
                for j in range(limit + 1):
                    dp[i][j] = dp[i-1][j]
                    if j >= v:
                        dp[i][j] += dp[i][j-v]
                    if j >= v * (c + 1):
                        dp[i][j] -= dp[i-1][j - v * (c + 1)]
                    dp[i][j] = (dp[i][j] + MOD) % MOD
            res = sum(dp[-1]) % MOD
            return max(res, 1) * (zero + 1) % MOD
        return (helper(r) - helper(l - 1) + MOD) % MOD
