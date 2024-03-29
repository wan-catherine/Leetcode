class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [i + 1 for i in range(length)]
        is_palindrome = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(i + 1):
                if s[i] == s[j] and (j == i or j + 1 == i or is_palindrome[j+1][i-1]):
                    is_palindrome[j][i] = 1
                    if j == 0:
                        dp[i] = 1
                    else:
                        dp[i] = min(dp[i], 1 + dp[j-1])
        return dp[-1] - 1

    def minCut_(self, s: str) -> int:
        length = len(s)
        if s == s[::-1]:
            return 0

        for i in range(1, length):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        dp = [i for i in range(-1, length)]
        for i in range(length):
            odd, even = 0, 0
            while i - odd >= 0 and i + odd < length and s[i - odd] == s[i + odd]:
                dp[i + odd + 1] = min(dp[i + odd + 1], dp[i - odd] + 1)
                odd += 1

            while i - even >= 0 and i + even + 1 < length and s[i - even] == s[i + even + 1]:
                dp[i + even + 2] = min(dp[i + even + 2], dp[i - even] + 1)
                even += 1
        return dp[-1]