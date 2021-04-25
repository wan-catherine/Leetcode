import heapq
from typing import List


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def check(th):
            nonlocal rows, cols
            if th < grid[0][0]:
                return False
            visited = set()
            visited.add((0,0))
            stack = [(0,0)]
            while stack:
                new_stack = []
                for r, c in stack:
                    if r == rows - 1 and c == cols - 1:
                        return True
                    for i, j in directions:
                        row, col = r+i, c+j
                        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] > th:
                            continue
                        visited.add((row, col))
                        new_stack.append((row, col))
                stack = new_stack
            return False

        left, right = 0, rows*cols
        while left < right:
            mid = (right - left) // 2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def swimInWater_dijkstra(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        res = [[50*50] * cols for _ in range(rows)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[0]*cols for _ in range(rows)]
        while pq:
            h, r, c = heapq.heappop(pq)
            # need to check this or it will be TLE
            # when visited[r][c] == 1, it means it was popped before , so now the value will be larger than before
            # no need to go next step.
            if visited[r][c]:
                continue
            visited[r][c] = 1
            res[r][c] = h
            if r == rows - 1 and c == cols - 1:
                break
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
                    continue
                heapq.heappush(pq, (max(grid[row][col], res[r][c]), row, col))
        return res[-1][-1]