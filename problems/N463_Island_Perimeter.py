class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 0:
                    continue
                perimeter += 4
                if row - 1 >= 0 and grid[row-1][col] == 1:
                    perimeter -= 1
                if row + 1 < row_len and grid[row+1][col] == 1:
                    perimeter -= 1
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    perimeter -= 1
                if col + 1 < col_len and grid[row][col+1] == 1:
                    perimeter -= 1
        return perimeter