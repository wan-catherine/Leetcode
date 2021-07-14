from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c, grid, num):
            if grid[r][c] != 1:
                return
            grid[r][c] = num
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                    continue
                dfs(row, col, grid, num)

        def check(r, c, num, pre):
            if grid2[r][c] != 1:
                return True
            grid2[r][c] = num
            ans = True if grid1[r][c] == pre else False
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or grid2[row][col] != 1:
                    continue
                ans = ans & check(row, col, num, pre)
            return ans

        one, two = 2, 2
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 1:
                    dfs(r, c, grid1, one)
                    one += 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    ans = check(r, c, two, grid1[r][c])
                    two += 1
                    if ans and grid1[r][c] not in [0, 1]:
                        res += 1
        return res
