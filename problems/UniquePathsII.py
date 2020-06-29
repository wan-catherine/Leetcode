class Solution:
    def uniquePathsWithObstacles_before(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid == None:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[n - 1][m - 1] == 1:
            return 0
        res = [[0] * m for i in range(n)]

        iflag = False
        for i in range(m):
            if obstacleGrid[0][i] == 1 or iflag:
                res[0][i] = 0
                iflag = True
            else:
                res[0][i] = 1
        iflag = False
        for i in range(n):
            if obstacleGrid[i][0] == 1 or iflag:
                res[i][0] = 0
                iflag = True
            else:
                res[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                    res[i][j] = 0
                elif obstacleGrid[i - 1][j] != 1 and obstacleGrid[i][j - 1] == 1:
                    res[i][j] = res[i - 1][j]
                elif obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] != 1:
                    res[i][j] = res[i][j - 1]
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[n - 1][m - 1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[1]* cols for _ in range(rows)]

        for row in range(rows):
            if obstacleGrid[row][0] == 1:
                j = row
                while j < rows:
                    dp[j][0] = 0
                    j += 1
                break

        for col in range(cols):
            if obstacleGrid[0][col] == 1:
                j = col
                while j < cols:
                    dp[0][j] = 0
                    j += 1
                break

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[-1][-1]

