"""
count the number of each row and col
and then find those isolated server
"""
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        row_count = [0] * rows
        col_count = [0] * cols
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    row_count[row] += 1
                    col_count[col] += 1
                    total += 1
        single = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and row_count[row] < 2 and col_count[col] < 2:
                    single += 1

        return total - single



