from typing import List
"""
Back in time, we consider from end to start. 
Union-find.

Also, we can use binary search . 
"""

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        parent = [i for i in range(row * col + 2)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if pp < pq:
                parent[pq] = pp
            else:
                parent[pp] = pq

        grid = [[0] * col for _ in range(row)]
        for i, j in cells:
            grid[i-1][j-1] = 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    continue
                if r == 0:
                    union(r * col + c, row * col)
                if r == row - 1:
                    union(r * col + c, row * col + 1)
                for i, j in directions:
                    ro, co = r + i, c + j
                    if ro < 0 or ro >= row or co < 0 or co >= col or grid[ro][co] == 1:
                        continue
                    union(r * col + c, ro * col + co)

        res = 0
        def check():
            return find(row*col) == find(row*col + 1)

        for p, q in cells[::-1]:
            if check():
                break
            r, c = p-1, q-1
            grid[r][c] = 0
            if r == 0:
                union(r * col + c, row * col)
            if r == row - 1:
                union(r * col + c, row * col + 1)
            for i, j in directions:
                ro, co = r + i, c + j
                if ro < 0 or ro >= row or co < 0 or co >= col or grid[ro][co] == 1:
                    continue
                union(r * col + c, ro * col + co)
            res += 1
        return len(cells) - res


