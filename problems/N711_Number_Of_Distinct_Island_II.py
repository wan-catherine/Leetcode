from typing import List

"""
The key part is how to get the shape after rotation (90, 180 or 270) or reflection (left/right or up/down) :
there are 8 situations: 
x, y
-x, y
x, -y
-x, -y
y, x 
-y, x 
y, -x 
-y, -x 
"""
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, cur):
            cur.append([r, c])
            grid[r][c] = 0
            for i, j in directions:
                row, col = r + i, c + j
                if row < 0 or row >= rows or col < 0 or col >= cols or not grid[row][col]:
                    continue
                grid[row][col] = 0
                dfs(row, col, cur)
        def shape(cur):
            rotate = [sorted([(x, y) for x, y in cur]),
                      sorted([(x, -y) for x, y in cur]),
                      sorted([(-x, y) for x, y in cur]),
                      sorted([(-x, -y) for x, y in cur]),
                      sorted([(y, x) for x, y in cur]),
                      sorted([(-y, x) for x, y in cur]),
                      sorted([(y, -x) for x, y in cur]),
                      sorted([(-y, -x) for x, y in cur]),
                      ]
            shapes = set()
            for li in rotate:
                rb, cb = li[0]
                shape = [(x-rb, y-cb) for x, y in li]
                shapes.add(tuple(shape))
            return shapes

        islands = set()
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                cur = []
                dfs(i, j, cur)
                cur.sort()
                rbase, cbase = cur[0]
                tmp = tuple(sorted([(x-rbase, y-cbase) for x, y in cur]))
                if tmp not in islands:
                    res += 1
                    shapes = shape(cur)
                    islands.update(shapes)
        return res