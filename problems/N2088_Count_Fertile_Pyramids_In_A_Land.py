from typing import List

"""
DP problem. 
Key point: 

For a cell grid[r][c], the largest radius of it when it as the lowest row of the pyramidal. 
If it can be 3 level pyramidal, then it can be a 2 level, 1 level . 
"""
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pyramidal = [[0] * cols for _ in range(rows)]
        res = 0
        for r in range(rows):
            left, right = [0] * cols, [0] * cols
            prev = 0
            for c in range(cols):
                if grid[r][c] == 0:
                    prev = 0
                    continue
                left[c] = prev + 1
                prev = left[c]
            prev = 0
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == 0:
                    prev = 0
                    continue
                right[c] = prev + 1
                prev = right[c]
            for c in range(cols):
                pyramidal[r][c] = min(left[c], right[c])

        up, down = [[0] * cols for _ in range(rows)], [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if pyramidal[r][c] == 0:
                    continue
                if r == 0:
                    up[r][c] = 1
                else:
                    up[r][c] = min(pyramidal[r][c], up[r-1][c] + 1)
                res += up[r][c] - 1
        for r in range(rows-1, -1, -1):
            for c in range(cols):
                if pyramidal[r][c] == 0:
                    continue
                if r == rows - 1:
                    up[r][c] = 1
                else:
                    up[r][c] = min(pyramidal[r][c], up[r+1][c] + 1)
                res += up[r][c] - 1
        return res
