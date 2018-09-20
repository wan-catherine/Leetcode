class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None:
            return 0

        n = len(grid)
        m = len(grid[0])

        res = [[0] * m for i in range(n)]
        res[0][0] = grid[0][0]
        for i in range(1, m):
            res[0][i] = res[0][i - 1] + grid[0][i]
        for i in range(1, n):
            res[i][0] = res[i - 1][0] + grid[i][0]

        for i in range(1,n):
            for j in range(1,m):
                before = res[i -1][j] if res[i -1][j] <= res[i][j - 1] else res[i][j - 1]
                res[i][j] = grid[i][j] + before

        return res[n - 1][m - 1]