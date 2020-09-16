"""
DP: how many different paths of moving at most N times to arrive (i,j).
dp[i][j] : total different paths to (i,j)

from 4 directions to move 1 step to arrive (i,j).
dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i+1][j] + dp[i][j+1]
need to consider boundary conditions.

Classical DP problem.
"""
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)]

        for k in range(N):
            temp = [row[:] for row in dp]
            for row in range(m):
                for col in range(n):
                    val = 0
                    for p, q in [(1,0),(0,1),(-1,0),(0,-1)]:
                        new_row,new_col = row+p, col+q
                        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                            val += 1
                        else:
                            val += dp[new_row][new_col]
                    temp[row][col] = val
            dp = temp
            print(dp)
        return dp[i][j] % (10**9 + 7)
