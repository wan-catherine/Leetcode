import collections
import sys
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        status = collections.defaultdict(int)
        visited = [[0] * cols for _ in range(rows)]
        stack = [(0, 0, 0)]
        res = sys.maxsize
        while stack:
            nstack = []
            for r, c, cost in stack:
                if visited[r][c] > 0 and status[(r, c)] < cost:
                    continue
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        continue
                    cur = cost
                    if grid[row][col] == 1:
                        cur += 1
                    if visited[row][col] > 0:
                        if status[(row, col)] <= cur:
                            continue
                    else:
                        visited[row][col] = 1
                    status[(row, col)] = cur
                    if row == rows - 1 and col == cols - 1:
                        res = min(res, cur)
                    nstack.append((row, col, cur))
            stack = nstack
        return res




