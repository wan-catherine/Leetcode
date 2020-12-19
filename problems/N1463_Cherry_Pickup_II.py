import sys
"""
We have two robots here and they need to arrive to the bottom row. 
So at least we need to dp[i][j], i,j is the col position for those two robots. 
Because the status only related to the previous row, so we can reuse the dp(copy it before modify). 
"""
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        # here we need to initialize as -sys.maxsize, because there are a lot of cells , Robert can't reach.
        dp = [[-sys.maxsize]* cols for _ in range(cols)]

        dp[0][cols-1] = grid[0][0] + grid[0][cols-1]

        for row in range(1, rows):
            previous = [x[:] for x in dp]
            for col1 in range(cols):
                for col2 in range(cols):
                    for a in [col1-1, col1, col1+1]:
                        for b in [col2-1, col2, col2+1]:
                            if a < 0 or a >= cols or b < 0 or b >= cols:
                                continue
                            if col1 != col2:
                                dp[col1][col2] = max(dp[col1][col2], previous[a][b] + grid[row][col1] + grid[row][col2])
                            else:
                                dp[col1][col2] = max(dp[col1][col2], previous[a][b] + grid[row][col1])
        return max([max(x) for x in dp])