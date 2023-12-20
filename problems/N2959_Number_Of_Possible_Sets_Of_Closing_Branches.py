import sys
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        res = 0
        for t in range(1 << n):
            dp = [[sys.maxsize]*n for _ in range(n)]
            for i in range(n):
                dp[i][i] = 0
            for road in roads:
                u, v, w = road
                if (1 << u) & t or (1 << v) & t:
                    continue
                for i in range(n):
                    if (1 << i) & t:
                        continue
                    for j in range(n):
                        if (1 << j) & t:
                            continue
                        dp[i][j] = min(dp[i][j], dp[i][u] + dp[v][j] + w, dp[i][v] + dp[u][j] + w)
            flag = 1
            for i in range(n):
                if (1 << i) & t:
                    continue
                for j in range(n):
                    if (1 << j) & t:
                        continue
                    if dp[i][j] > maxDistance:
                        flag = 0
                        break
                if flag == 0:
                    break
            res += flag
        return res

