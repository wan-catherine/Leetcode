import collections
import sys
from typing import List


class Solution:
    """
    TLE
    dp[i][d] : xor of the first i numbers equals d .
    xor is a time-consuming operation for python  .
    """
    def minChanges(self, nums: List[int], k: int) -> int:
        costs = [collections.defaultdict(int) for _ in range(k)]
        total = [0] * k
        length = len(nums)
        for i in range(length):
            costs[i % k][nums[i]] += 1
            total[i % k] += 1
        n = 2 ** 10
        dp = [[sys.maxsize] * n for _ in range(k)]
        for d in range(n):
            dp[0][d] = total[0] - costs[0][d]

        for i in range(1, k):
            dmin = sys.maxsize
            x = None
            for d in range(n):
                if dp[i - 1][d] < dmin:
                    dmin = dp[i - 1][d]
                    x = d

            for d in range(n):
                # if v not in costs[i]
                dp[i][d] = min(dp[i][d], dmin + total[i] - costs[i][x^d])

                # if v in costs[i]
                for v in costs[i]:
                    dp[i][d] = min(dp[i][d], dp[i - 1][d ^ v] + total[i] - costs[i][v])

        return dp[-1][0]


    """
    Accepted. 
    dp[i][j] : the most number of value not change for xor equals to j . 
    """
    def minChanges(self, nums: List[int], k: int) -> int:
        costs = [collections.defaultdict(int) for _ in range(k)]
        length = len(nums)
        for i in range(length):
            costs[i % k][nums[i]] += 1
        n = 2 ** 10
        dp = [[0] * n for _ in range(k+1)]
        for d in range(1, n):
            dp[0][d] = -sys.maxsize

        for i in range(1, k+1):
            maximum = max(dp[i-1])
            for j in range(n):
                for d in costs[i-1]:
                    dp[i][j] = max(dp[i][j], maximum, dp[i-1][d^j] + costs[i-1][d])
        return length - dp[-1][0]

