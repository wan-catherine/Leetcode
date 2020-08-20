class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == '':
            return len(word2)
        if word2 == '':
            return len(word1)

        cols = len(word1)
        rows = len(word2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1,cols+1):
            dp[0][i] = i

        for i in range(1, rows+1):
            dp[i][0] = i

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                diagonal = dp[i-1][j-1] + (2 if word2[i-1] != word1[j-1] else 0)
                dp[i][j] = min(diagonal, dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]