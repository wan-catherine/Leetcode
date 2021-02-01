class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
            if i+1 < length and s[i] == s[i+1]:
                dp[i][i+1] = True

        for i in range(length-1, -1, -1):
            for j in range(i+2, length):
                dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else False

        for i in range(1, length):
            for j in range(i, length-1):
                if dp[0][i-1] and dp[i][j] and dp[j+1][length-1]:
                    return True
        return False
