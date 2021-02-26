"""
This problem is similiar as : give a string, use dp to get the largest palindrome.
Just add one more condition : i < l1, j > l1.

Classical interval DP!!!
"""
class Solution(object):
    def longestPalindrome(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        word = word1 + word2
        length = l1 + l2
        dp = [[0] * length for _ in range(length)]
        res = 0
        for i in range(length):
            dp[i][i] = 1

        for l in range(2, length+1):
            for i in range(length-l+1):
                j = i + l - 1
                if word[i] == word[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i < l1 and j >= l1:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return res