class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
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