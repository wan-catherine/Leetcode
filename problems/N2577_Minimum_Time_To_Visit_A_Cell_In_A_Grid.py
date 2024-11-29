import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        visited = [[-1] * cols for _ in range(rows)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pq = []
        if grid[0][1] <= 1:
            heapq.heappush(pq, (1, 0, 1))
        if grid[1][0] <= 1:
            heapq.heappush(pq, (1, 1, 0))
        while pq:
            t, r, c = heapq.heappop(pq)
            if visited[r][c] != -1:
                continue
            visited[r][c] = t
            if r == rows - 1 and c == cols - 1:
                break
            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or visited[nx][ny] != -1:
                    continue
                if grid[nx][ny] <= t + 1:
                    heapq.heappush(pq, (t+1, nx, ny))
                elif (grid[nx][ny] - t) % 2 == 0:
                    heapq.heappush(pq, (grid[nx][ny] + 1, nx, ny))
                else:
                    heapq.heappush(pq, (grid[nx][ny], nx, ny))
        return visited[-1][-1]
