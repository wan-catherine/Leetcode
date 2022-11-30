class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = {'2', '3', '5', '7'}
        MOD = 10 ** 9 + 7
        length = len(s)
        s = '#' + s
        dp = [[0] * (k + 1) for _ in range(length + 1)]
        dp[0][0] = 1
        # for i in range(1, length + 1):
        #     for j in range(1, min(i, k + 1)):
        #         if s[i] in primes or i - minLength < 0:
        #             continue
        #         for p in range(i-minLength, (j-1) * minLength-1, -1):
        #             if s[p+1] not in primes:
        #                 continue
        #             dp[i][j] += dp[p][j-1]
        for j in range(1, k + 1):
            cur = 0
            for i in range(1, length + 1):
                if i - minLength >= 0 and s[i-minLength] not in primes and s[i-minLength+1] in primes:
                    cur += dp[i-minLength][j-1]
                if s[i] not in primes:
                    dp[i][j] = cur
        return dp[-1][-1] % MOD
