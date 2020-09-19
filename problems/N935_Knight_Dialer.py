class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapping = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        dp = [[0]*10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(10):
                for n in mapping[j]:
                    dp[i][j] += dp[i-1][n]
        return sum(dp[-1]) % (10 ** 9 + 7)
