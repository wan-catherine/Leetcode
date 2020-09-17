class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]

        asc1 = [ord(c) for c in s1]
        asc2 = [ord(c) for c in s2]
        for i in range(1, l1+1):
            if dp[i-1][1]:
                dp[i][1] = dp[i-1][1]
            elif asc1[i-1] == asc2[0]:
                dp[i][1] = asc1[i-1]

        for i in range(1, l2+1):
            if dp[1][i-1]:
                dp[1][i] = dp[1][i-1]
            elif asc2[i-1] == asc1[0]:
                dp[1][i] = asc1[0]

        for i in range(2, l1+1):
            for j in range(2, l2+1):
                row, col = i-1, j-1
                if asc1[row] == asc2[col]:
                    dp[i][j] = dp[i-1][j-1] + asc1[row]
                dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

        return sum(asc1) + sum(asc2) - 2 * dp[-1][-1]

