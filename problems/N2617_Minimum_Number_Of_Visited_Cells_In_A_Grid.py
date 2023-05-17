import bisect
import heapq
import sys
from typing import List

"""
difference array 
"""

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[sys.maxsize] * cols for _ in range(rows)]
        rdiff = [[] for _ in range(rows)]
        rset = [[] for _ in range(rows)]
        cdiff = [[] for _ in range(cols)]
        cset = [[] for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                while rdiff[i] and rdiff[i][0][0] == j:
                    r, rd = heapq.heappop(rdiff[i])
                    if rd > 0:
                        bisect.insort(rset[i], rd)
                    else:
                        idx = bisect.bisect_left(rset[i], -rd)
                        del rset[i][idx]  # del is faster than next line
                        # rset[i] = rset[i][:idx] + rset[i][idx+1:]

                while cdiff[j] and cdiff[j][0][0] == i:
                    c, cd = heapq.heappop(cdiff[j])
                    if cd > 0:
                        bisect.insort(cset[j], cd)
                    else:
                        idx = bisect.bisect_left(cset[j], -cd)
                        del cset[j][idx]
                        # cset[j] = cset[j][:idx] + cset[j][idx+1:]

                if len(rset[i]) > 0:
                    dp[i][j] = min(dp[i][j], rset[i][0])
                if len(cset[j]) > 0:
                    dp[i][j] = min(dp[i][j], cset[j][0])

                if i == 0 and j == 0:
                    dp[i][j] = 0

                step = grid[i][j]
                if step == 0:
                    continue
                if j + 1 < cols:
                    heapq.heappush(rdiff[i], (j + 1, dp[i][j] + 1))
                if j + step + 1 < cols:
                    heapq.heappush(rdiff[i], (j + step + 1, -(dp[i][j] + 1)))
                if i + 1 < rows:
                    heapq.heappush(cdiff[j], (i + 1, dp[i][j] + 1))
                if i + step + 1 < rows:
                    heapq.heappush(cdiff[j], (i + step + 1, -(dp[i][j] + 1)))

        if dp[-1][-1] == sys.maxsize:
            return -1
        return dp[-1][-1] + 1



