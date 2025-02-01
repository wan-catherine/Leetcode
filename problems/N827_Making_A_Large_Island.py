import collections
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0] * n for _ in range(n)]
        def dfs(r, c, v):
            if visited[r][c]:
                return 0
            ans = 1
            visited[r][c] = True
            grid[r][c] = v
            for i, j in directions:
                row, col = i + r, j + c
                if row < 0 or row >= n or col < 0 or col >= n or grid[row][col] == 0 or visited[row][col]:
                    continue
                grid[row][col] = v
                ans += dfs(row, col, v)
            return ans
        status = collections.defaultdict(int)
        c = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    c += 1
                    status[c] = dfs(i, j, c)

        res = max(status.values()) if len(status) > 0 else 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] > 0:
                    continue
                ans = 1
                s = set()
                for i, j in directions:
                    row, col = i + r, j + c
                    if row < 0 or row >= n or col < 0 or col >= n or grid[row][col] == 0:
                        continue
                    s.add(grid[row][col])
                for v in s:
                    ans += status[v]
                res = max(res, ans)
        return res


