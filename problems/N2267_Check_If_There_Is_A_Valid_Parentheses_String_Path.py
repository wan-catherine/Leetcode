from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]
        dp[0][0] = set([1])
        for i in range(1, n):
            if grid[0][i] == '(':
                c = 1
            else:
                c = -1
            ns = set()
            for j in dp[0][i-1]:
                if j + c < 0:
                    continue
                ns.add(j + c)
            dp[0][i] = ns
        for i in range(1, m):
            if grid[i][0] == '(':
                c = 1
            else:
                c = -1
            ns = set()
            for j in dp[i-1][0]:
                if j + c < 0:
                    continue
                ns.add(j + c)
            dp[i][0] = ns
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == '(':
                    c = 1
                else:
                    c = -1
                ns = set()
                for p in dp[i-1][j]:
                    if p + c < 0:
                        continue
                    ns.add(p + c)
                for p in dp[i][j-1]:
                    if p + c < 0:
                        continue
                    ns.add(p + c)
                dp[i][j] = ns
        return True if 0 in dp[-1][-1] else False
