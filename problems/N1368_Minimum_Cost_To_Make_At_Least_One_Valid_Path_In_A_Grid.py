import sys
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        step = 0
        stack = []
        def flow(r, c, arr):
            if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                return
            visited[r][c] = 1
            arr.append((r, c))
            if grid[r][c] == 1:
                flow(r, c + 1, arr)
            elif grid[r][c] == 2:
                flow(r, c - 1, arr)
            elif grid[r][c] == 3:
                flow(r+1, c, arr)
            else:
                flow(r-1, c, arr)
        flow(0,0, stack)
        while stack:
            nstack = []
            for r, c in stack:
                if r == m - 1 and c == n - 1:
                    return step
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= m or col < 0 or col >= n or visited[row][col]:
                        continue
                    flow(row, col, nstack)
            step += 1
            stack = nstack
        return step


