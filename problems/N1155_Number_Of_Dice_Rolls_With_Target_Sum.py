class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d*f < target:
            return 0

        dp = [[0]*(target+1) for _ in range(d+1)]
        for i in range(1, min(f, target)+1):
            dp[1][i] = 1

        for i in range(2, d+1):
            for j in range(1, target+1):
                for k in range(1, f+1):
                    if j-k>0:
                        dp[i][j] += dp[i-1][j-k]
        return dp[-1][-1] % (10**9 + 7)