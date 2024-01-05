import sys
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        res = sys.maxsize
        def dfs(cur, moves):
            nonlocal res
            if moves >= res:
                return
            if cur >= 9:
                res = min(res, moves)
                return
            r, c = cur // 3 , cur % 3
            if grid[r][c] != 0:
                dfs(cur + 1, moves)
                return

            for i in range(3):
                for j in range(3):
                    if grid[i][j] <= 1:
                        continue
                    grid[i][j] -= 1
                    grid[r][c] += 1
                    dfs(cur + 1, moves + abs(r - i) + abs(c - j))
                    grid[i][j] += 1
                    grid[r][c] -= 1

        dfs(0, 0)
        return res
