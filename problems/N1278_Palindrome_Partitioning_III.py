import sys
"""
dp[i][j] : the minimal number of characters that I need to change to divide s[:i+1] into j non-empty disjoint substrings. 
dp[i][j] = min{ dp[m-1][j-1] + count(s[m:i+1]) } 
count : the number of characters that need to change to make s[m:i+1] a palindrome. 
"""

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)
        dp = [[sys.maxsize]*(k+1) for _ in range(length+1)]
        dp[0][0] = 0
        s = '@' + s
        def helper(start, end):
            count = 0
            while start < end:
                if s[start] != s[end]:
                    count+= 1
                start += 1
                end -= 1
            return count

        """
        interval dp problem. 
        From a small interval to get the larger interval
        count[i][j] == count[i+1][j-1] + (1 if s[i] != s[j] else 0)
        """
        count = [[0] * (length+1) for _ in range(length+1)]
        for i in range(length+1):
            count[i][i] = 0
        for l in range(2, length + 1):
            for i in range(1, length-l+2):
                j = i + l - 1
                if s[i] == s[j]:
                    count[i][j] = count[i+1][j-1]
                else:
                    count[i][j] = count[i+1][j-1] + 1

        for i in range(1, length+1):
            for j in range(1, min(i+1,k+1)):
                for m in range(j, i+1):
                    # dp[i][j] = min(dp[i][j], dp[m-1][j-1] + helper(m, i))
                    dp[i][j] = min(dp[i][j], dp[m - 1][j - 1] + count[m][i])

        return dp[-1][-1]