class Solution:
    def findIntegers(self, num: int) -> int:
        if num == 0:
            return 0
        if num == 1:
            return 2
        dp = [0] * 33
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 33):
            dp[i] = dp[i-1] + dp[i-2]

        digits = [0] * 33
        j = 1
        while num:
            digits[j] = num % 2
            j += 1
            num //= 2
        ans = 0
        i = 32
        while i > 0:
            if digits[i] == 0:
                i -= 1
                continue
            # ith == 0
            ans += dp[i-1]

            # ith == 1
            # i-1 th == 0
            if i >= 2 and digits[i-1] == 1:
                ans += dp[i-2]
                return ans
            else:
                i -= 2

        ans += 1
        return ans
