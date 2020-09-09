class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [i + 1 for i in range(length)]
        for i in range(1, length):
            if self.is_palindrome(s[:i + 1]):
                dp[i] = 1
                continue
            for j in range(i):
                if self.is_palindrome(s[j + 1:i + 1]):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1] - 1

    def is_palindrome(self, s):
        return s == s[::-1]