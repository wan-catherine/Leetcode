class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 2
        res = n - 1
        while i <= n // 2:
            j = n // i
            if n == i * j:
                temp = j ** i
            elif n == j * (i - 1) + j + 1:
                temp = j ** (i - 1) * (j + 1)
            elif n == (j + 1)*(i - 1) + j:
                temp = (j + 1) ** (i - 1) * j

            res = max(temp, res)
            i += 1
        return res

    def integerBreak_dp(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * (n + 1)
        # base caee : at least i//2 >= 2 , so we need dp[2], dp[3] here .
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])
        return dp[-1]