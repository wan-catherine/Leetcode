"""
dp[i][j]: the minimum number of turns the printer needed in order to print s[i:j+1].
[axxxx] a [xxxx]
        k
[axxxxxxxx] a
            k  ==> k == j ==> dp[k+1][j] = 0
-> when we print a, we can print all the string, then we can save one turn for the next a.
dp[i][j] = min(dp[i][k-1] + dp[k+1][j]) for all i< k <=j , s[k] == s[i]
"""
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        length = len(s)
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i + l - 1
                dp[i][j] = 1 + dp[i+1][j]
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + (dp[k+1][j] if k+1<=j else 0))
        return dp[0][length-1]