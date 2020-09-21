import sys
from functools import lru_cache
from math import inf


class Solution(object):
    def connectTwoGroups_tle(self, cost):
        """
        :type cost: List[List[int]]
        :rtype: int
        """
        l, r = len(cost), len(cost[0])
        dp = [[float(inf)] * 2**r for _ in range(l)]
        for i in range(1, 2**r):
            val = 0
            for j in range(r):
                if (i >> j) & 1:
                    val += cost[0][j]
            dp[0][i] = val
        minimum = [min(cost[i]) for i in range(l)]
        for i in range(1, l):
            for j in range(1, 2**r):
                subset = j
                while subset > 0:
                    val = 0
                    for k in range(r):
                        if (subset >> k) & 1:
                            val += cost[i][k]
                    dp[i][j] = min(dp[i][j], dp[i-1][j-subset]+val)
                    subset = (subset - 1)&j
                dp[i][j] = min(dp[i][j], dp[i-1][j] + minimum[i])
        return dp[-1][-1]

    def connectTwoGroups(self, cost):
        l, r = len(cost), len(cost[0])
        minimum_r = [sys.maxsize] * r
        for j in range(r):
            for i in range(l):
                minimum_r[j] = min(minimum_r[j], cost[i][j])
        memo = {}
        # @lru_cache(None)
        def dfs(i, mask):
            if (i, mask) in memo:
                return memo[(i, mask)]
            if i == l:
                ans = 0
                for j in range(r):
                    if mask & (1 << j) == 0:
                        ans += minimum_r[j]
                memo[(i, mask)] = ans
                return ans

            ans = sys.maxsize
            for j in range(r):
                ans = min(ans, dfs(i+1, mask|(1 << j)) + cost[i][j])
            memo[(i, mask)] = ans
            return ans

        res = dfs(0, 0)
        # print(memo)
        return res
