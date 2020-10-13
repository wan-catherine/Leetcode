"""
consider from '1' not '0'
"""
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        stack = []
        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    grid[i][j] = 2

        step = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            new_stack = []
            for i, j in stack:
                for r, c in directions:
                    row, col = r+i, c+j
                    if row < 0 or row >= n or col < 0 or col >= n:
                        continue
                    if grid[row][col] == 0:
                        res = max(res, step + 1)
                        grid[row][col] = 2
                        new_stack.append((row, col))
                        continue
                    if grid[row][col] == 2:
                        continue
            stack = new_stack
            step += 1
        return res

