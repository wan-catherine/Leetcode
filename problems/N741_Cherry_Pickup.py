import sys
"""
We need to find two path from [0,0] to [n-1,n-1].
So we need to set up i, j, p, q to mark all those status ==> dp[i][j][p][q]. 
But here for those two points , they always move to same steps : i+j = p+q. 
So we only need three dimention here : q = i+j-p
"""

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        n = length + 1
        dp = [[[-sys.maxsize]*n for _ in range(n)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, n):
                if grid[i-1][j-1] == -1:
                    continue
                for p in range(1, n):
                    q = i+j-p
                    if q < 1 or q > length:
                        continue
                    if grid[p-1][q-1] == -1:
                        continue
                    if i == 1 and j == 1 and p == 1:
                        dp[i][j][p] = grid[0][0]
                        continue
                    if i == p and j == q:
                        dp[i][j][p] = max(dp[i][j][p], max(dp[i-1][j][p-1],dp[i-1][j][p],dp[i][j-1][p-1],dp[i][j-1][p])+grid[i-1][j-1])
                    else:
                        dp[i][j][p] = max(dp[i][j][p], max(dp[i - 1][j][p - 1], dp[i - 1][j][p],
                                                                 dp[i][j - 1][p - 1], dp[i][j - 1][p]) +
                                             grid[i - 1][j - 1] + grid[p-1][q-1])

        # print(dp)
        return max(0, dp[-1][-1][-1])



