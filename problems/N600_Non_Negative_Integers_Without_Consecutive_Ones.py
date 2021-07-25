class Solution:
    def findIntegers_before(self, num: int) -> int:
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

    def findIntegers(self, n: int) -> int:
        num = bin(n)[2:]
        length = len(num)
        if length == 1:
            return 1 if num == '0' else 2
        dp = [0] * (length + 1)
        dp[1], dp[2] = 2, 1
        for i in range(3, length + 1):
            for j in range(1, i - 1):
                dp[i] += dp[j]
        for i in range(1, length + 1):
            dp[i] += dp[i-1]
        def helper(snum, is_prev_one):
            if snum == '0':
                return 1
            if snum == '1':
                return 1 if is_prev_one else 2
            # if snum[0] == '0', we need to recursive call helper
            if snum[0] == '0':
                return helper(snum[1:], False)
            # if snum[0] == '1' which means we can use dp[len(snum[1:])] directly .
            if is_prev_one:
                return dp[len(snum) - 1]
            ans = dp[len(snum) - 1]
            ans += helper(snum[1:], True)
            return ans
        return helper(num, False)
