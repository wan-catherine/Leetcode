import sys
from typing import List

"""
From two ends to middle, so it can be divided to subproblems. 
dp[i][j][k] : the minimum cost when the ith color is j and (length - i -1)th color is k. 
"""
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        prev = [[0] * 3 for _ in range(3)]
        cur = [[sys.maxsize] * 3 for _ in range(3)]

        for i in range(n // 2):
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue
                    val = cost[i][j] + cost[n - i - 1][k]
                    for p in range(3):
                        for q in range(3):
                            if p == q or p == j or q == k:
                                continue
                            cur[j][k] = min(cur[j][k], val + prev[p][q])
            prev = cur
            cur = [[sys.maxsize] * 3 for _ in range(3)]
        return min(min(v) for v in prev)

