import sys
from typing import List

"""
dp[i][j][k] : minimum price to split stones[i~j] into k groups. 
after we have k groups, then next step , combine them into one group : 
dp[i][j][1] = dp[i][j][k] + sums(stones[i~j])
"""
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        length = len(stones)
        if length == K:
            return sum(stones)
        if (length-1) % (K-1):
            return - 1

        prefix = [0] + stones[:]
        for i in range(length):
            prefix[i+1] += prefix[i]

        dp = [[[sys.maxsize] * (K+1) for _ in range(length)] for _ in range(length)]

        for i in range(length):
            dp[i][i][1] = 0

        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                for k in range(2, K+1):
                    if k > l:
                        continue
                    for m in range(i, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][m][1] + dp[m+1][j][k-1])
                if dp[i][j][K] != sys.maxsize:
                    dp[i][j][1] = dp[i][j][K] + prefix[j+1] - prefix[i]
        if dp[0][-1][1] == sys.maxsize:
            return -1
        return dp[0][-1][1]



