class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if not poured:
            return 0
        dp = [[0]*100 for _ in range(100)]

        dp[0][0] = poured
        for i in range(1,100):
            for j in range(i):
                dp[i][j] += max(0, (dp[i-1][j] - 1)/ 2)
                dp[i][j+1] += max(0, (dp[i-1][j] - 1)/ 2)
            if i >= query_row:
                break
        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1.0 else 1.0