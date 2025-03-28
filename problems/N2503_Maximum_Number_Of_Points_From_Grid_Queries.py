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

    def maxPoints_20250328(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lq = len(queries)
        que = [(queries[i], i) for i in range(lq)]
        que.sort(key=lambda x: x[0])
        res = [0] * lq
        cur = 0
        stack = [(0,0)]
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        memo = {}
        for v, idx in que:
            if v in memo:
                res[idx] = memo[v]
                continue
            left = []
            while True:
                nstack = []
                for r, c in stack:
                    if grid[r][c] >= v:
                        left.append((r, c))
                        continue
                    cur += 1
                    for i, j in directions:
                        row, col = r + i, c + j
                        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
                            continue
                        nstack.append((row, col))
                        visited[row][col] = True
                if not nstack:
                    break
                stack = nstack
            stack = left
            memo[v] = cur
            res[idx] = cur
        return res