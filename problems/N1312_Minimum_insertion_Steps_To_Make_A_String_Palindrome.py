class Solution:
    def minInsertions(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        dp[0][0] = 1
        for i in range(1, length):
            dp[i][i] = 1
            if s[i-1] == s[i]:
                dp[i-1][i] = 2
            else:
                dp[i-1][i] = 1

        for l in range(3, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
                else:
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
        return length - dp[0][-1]