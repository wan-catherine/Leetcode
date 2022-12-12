import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        qes = sorted(queries)
        res = {}
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited= set()
        visited.add((0,0))
        pq = [(grid[0][0], 0, 0)]
        for q in qes:
            while pq:
                v, r, c = pq[0]
                if v >= q:
                    break
                heapq.heappop(pq)
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
                        continue
                    visited.add((row, col))
                    heapq.heappush(pq, (grid[row][col], row, col))
            res[q] = len(visited) - len(pq)
        return [res[q] for q in queries]