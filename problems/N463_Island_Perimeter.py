class Solution(object):
    def islandPerimeter_before(self, grid):
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

    def islandPerimeter(self, grid):
        res = 0
        stack = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.add((i, j))
                    break
            if len(stack) > 0:
                break
        while stack:
            i, j = stack.pop()
            res += 4
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                stack.add((i - 1, j))
                res -= 2
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                stack.add((i + 1, j))
                res -= 2
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                stack.add((i, j - 1))
                res -= 2
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                stack.add((i, j + 1))
                res -= 2
        return res