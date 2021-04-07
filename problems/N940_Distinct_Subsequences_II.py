class Solution:
    def distinctSubseqII(self, S: str) -> int:
        length = len(S)
        dp = [0] * (length + 1)
        dp[0] = 1
        arr = [0] * 26
        m = 10**9+7
        for i in range(1, length + 1):
            dp[i] = 2 * dp[i-1]
            index = ord(S[i-1]) - ord('a')
            if arr[index]:
                dp[i] -= dp[arr[index] - 1]
            dp[i] %= m
            arr[index] = i
        return dp[-1] - 1