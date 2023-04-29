from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c):
            cur = grid[r][c]
            grid[r][c] = 0
            for i, j in directions:
                rr, cc = r + i, c + j
                if rr < 0 or rr >= row or cc < 0 or cc >= col or grid[rr][cc] == 0:
                    continue
                cur += dfs(rr, cc)
            return cur
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                res = max(res, dfs(i, j))
        return res