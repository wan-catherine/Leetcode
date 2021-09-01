"""
similar as 940.
The only point here is we need to find the k which the first index that is 1 not 0.
This way we can make sure all other will starts will '1'.

dp[i] : till index i, the number of unique good subsequece .
"""
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        binary = '#' + binary
        length = len(binary)
        dp = [0] * length
        k = 1
        while k < length and binary[k] == '0':
            k += 1
        if k == length:
            return 1
        dp[k] = 1
        one, zero = 0, 0
        for i in range(k+1, length):
            dp[i] = 2 * dp[i-1]
            if binary[i] == '0':
                dp[i] -= dp[zero-1] if zero > 0 else 0
                zero = i
            else:
                dp[i] -= dp[one-1] if one > 0 else 0
                one = i
        return (dp[-1] + (1 if '0' in binary else 0)) % (10**9+7)

