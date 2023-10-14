import sys


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        arr = []
        for idx, i in enumerate(s1):
            if i != s2[idx]:
                arr.append(idx)
        length = len(arr)
        if length % 2:
            return -1
        arr = [0] + arr
        dp = [[sys.maxsize] * (length + 1) for _ in range(length + 1)]
        dp[0][0] = 0

        for i in range(1, length + 1):
            for j in range(2):
                if i - 2 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-2][j] + min(x, arr[i] - arr[i-1]))
                if j + 1 <= i - 1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + x)
        return dp[length][0]


