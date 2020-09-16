class Solution(object):
    # dp[i][j] : the number of paths from all legal location to location[i,j]
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0:
            return 1.0
        dp = [[1]*N for _ in range(N)]

        for k in range(K):
            dp_new = [[0]*N for _ in range(N)]
            for row in range(N):
                for col in range(N):
                    for i, j in [(2,1),(1,2),(2,-1),(1,-2),(-2,-1),(-1,-2),(-2,1),(-1,2)]:
                        new_row, new_col = row+i, col+j
                        if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                            continue
                        dp_new[row][col] += dp[new_row][new_col]
            dp = dp_new
        return dp[r][c] / 8 ** K

    # dp[i][j] : the number of paths from original location to location[i,j]
    def knightProbability_(self, N, K, r, c):
        if K == 0:
            return 1.0
        dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        for k in range(K):
            dp_new = [[0] * N for _ in range(N)]
            for row in range(N):
                for col in range(N):
                    for i, j in [(2,1),(1,2),(2,-1),(1,-2),(-2,-1),(-1,-2),(-2,1),(-1,2)]:
                        new_row, new_col = row + i, col + j
                        if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                            continue
                        dp_new[row][col] += dp[new_row][new_col]
            dp = dp_new
        res = 0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        return res / 8 ** K