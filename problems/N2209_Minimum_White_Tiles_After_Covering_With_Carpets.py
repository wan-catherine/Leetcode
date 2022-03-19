"""
DP:
dp[i][j] : the minimum number of white tile still visible for ith floor by using j number of carpet .

Two options :
1. do nothing about the ith tile : dp[i-1][j] + int(floor[i])
2. cover it by a carpet : dp[i-carpetLen][j]

"""

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        length = len(floor)
        if numCarpets * carpetLen >= length:
            return 0
        dp = [[0] * (numCarpets + 1) for _ in range(length + 1)]
        for i in range(length):
            dp[i+1][0] = dp[i][0] + int(floor[i])
        for i in range(length):
            for j in range(numCarpets):
                dp[i+1][j+1] = min(dp[i][j+1] + int(floor[i]), dp[max(i+1-carpetLen, 0)][j])
        return dp[-1][-1]
