"""
dp[i] : minimum number of operations for getting i As.
j from 2 to i, if i % 2 == 0, then we can paste it and copy.
"""
class Solution(object):
    def minSteps_dp(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(2, i+1):
                if i % j:
                    continue
                k = i // j
                dp[i] = min(dp[i], dp[k] + 1 + j - 1)
                break
        return dp[-1]

    # greedy
    def minSteps(self, n):
        res = 0
        for i in range(2, n+1):
            while not n % i:
                res += i
                n //= i
        return res
