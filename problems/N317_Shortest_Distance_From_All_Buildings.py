import sys
from typing import List

"""
Similar as 296. 
The main different is here we have some obstacles which means some index we might can't arrive. 
For 296, the distance for each point is confirmed .
But here not. So we need to use BFS.
"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        count = [[0] * cols for _ in range(rows)]
        building_num = 0
        def bfs(r, c, visited):
            stack = [(r,c)]
            step = 0
            while stack:
                new_stack = []
                step += 1
                for rr, cc in stack:
                    for i, j in directions:
                        row, col = rr + i, cc + j
                        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] > 0:
                            continue
                        visited[row][col] = 1
                        count[row][col] += 1
                        grid[row][col] -= step
                        new_stack.append((row, col))
                stack = new_stack

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                building_num += 1
                visited = [[0] * cols for _ in range(rows)]
                visited[i][j] = 1
                bfs(i, j, visited)
        res = -sys.maxsize
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0 and count[i][j] == building_num:
                    res = max(res, grid[i][j])
        return abs(res) if res != -sys.maxsize else -1