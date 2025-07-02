from itertools import groupby


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        groups = [len(list(group)) for _, group in groupby(word)]

        ways = 1
        for n in groups:
            ways = (ways * n) % MOD

        if len(groups) >= k:
            return ways

        prefix = [1] * k

        for g in groups:
            dp = [0] * k
            for l in range(1, k):
                dp[l] = prefix[l - 1]
                if l - g - 1 >= 0:
                    dp[l] = (dp[l] - prefix[l - g - 1]) % MOD

            prefix = dp[:]
            for i in range(1, k):
                prefix[i] = (prefix[i - 1] + prefix[i]) % MOD

        return (ways - prefix[k - 1]) % MOD