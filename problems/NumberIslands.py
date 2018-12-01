class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                count += 1
                self.dfs(grid, i, j, rows, cols, directions)

        return count

    def dfs(self, grid, i, j, rows, cols, directions):
        if i < 0 or i > rows -1 or j < 0 or j > cols - 1:
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        for m, n in directions:
            self.dfs(grid, i+m, j+n, rows, cols, directions)


