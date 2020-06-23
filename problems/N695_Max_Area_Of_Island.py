class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 0:
                    continue
                res = max(res, self.dfs(grid, 1, row, col))
        return res


    def dfs(self, grid, res, row, col):
        if grid[row][col] == 0:
            return res
        grid[row][col] = 0
        for x,y in self.directions:
            if row+x < 0 or row+x >= self.rows or col+y < 0 or col+y >= self.cols:
                continue
            if grid[row+x][col+y] == 0:
                continue
            res += 1
            res = self.dfs(grid, res, row+x, col+y)
        return res
