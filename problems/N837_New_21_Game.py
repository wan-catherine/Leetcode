class Solution(object):
    def new21Game_tle(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        memo = {}
        def dfs(current):
            if current in memo:
                return memo[current]

            if current >= K:
                if current > N:
                    return 0
                else:
                    return 1

            res = 0
            for i in range(1, W+1):
                res += dfs(current+i)
            memo[current] = res/W
            return memo[current]

        return dfs(0)

    """
    dp[i] : the probability of get point i
    In order to get point i , Alice can draw number and gains an integer between 1~W.
    so : dp[i] = dp[i-1] * (probability of get 1) + dp[i-2] * (probability of get 2) + ... + dp[i-w] * (probability of get W)
            = (dp[i-1] + ... + dp[i-W]) * 1 / W
    The next is a sliding window
    """
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W:
            return 1
        dp = [0] * (N+1)
        dp[0] = 1
        win_sum = 0
        for i in range(1, N+1):
            if i - 1 < K:
                win_sum += dp[i-1]
            if i - W - 1 >= 0:
                win_sum -= dp[i-W-1]
            dp[i] = win_sum / W
        return sum(dp[K:])

