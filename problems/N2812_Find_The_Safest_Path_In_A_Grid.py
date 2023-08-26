from typing import List

"""
Very good one !!!
A classical BFS
"""

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        thieves = []
        length = len(grid)
        for i in range(length):
            for j in range(length):
                if grid[i][j] == 1:
                    thieves.append((i, j))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cur = 0
        while thieves:
            nstack = []
            for ii, jj in thieves:
                for i, j in directions:
                    r = ii + i
                    c = jj + j
                    if r < 0 or r >= length or c < 0 or c >= length or grid[r][c] != 0:
                        continue
                    grid[r][c] = grid[ii][jj] + 1
                    nstack.append((r, c))
            cur += 1
            thieves = nstack

        def check(num):
            stack = [(0,0)]
            visited = [[0] * length for _ in range(length)]
            visited[0][0] = 1
            while stack:
                nstack = []
                for r, c in stack:
                    if grid[r][c] <= num:
                        continue
                    if r == length - 1 and c == length - 1:
                        return True
                    for i, j in directions:
                        rr, cc = r + i, c + j
                        if rr < 0 or rr >= length or cc < 0 or cc >= length or visited[rr][cc] == 1 or grid[rr][cc] <= num:
                            continue
                        visited[rr][cc] = 1
                        nstack.append((rr, cc))
                stack = nstack
            return False

        l, r = 0, min(grid[0][0], grid[-1][-1]) + 1
        while l < r:
            mid = (r - l + 1) // 2 + l
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l