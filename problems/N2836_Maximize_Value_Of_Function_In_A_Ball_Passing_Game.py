import math
from typing import List

"""
Binary lifting
"""

class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        length = len(receiver)
        kk = k
        up = 0
        while kk > 0:
            up += 1
            kk //= 2

        dp = [[0] * up for _ in range(length)]
        pos = [[0] * up for _ in range(length)]

        for i in range(length):
            dp[i][0] = receiver[i]
            pos[i][0] = receiver[i]

        for j in range(1, up):
            for i in range(length):
                pos[i][j] = pos[pos[i][j-1]][j-1]
                dp[i][j] = dp[pos[i][j-1]][j-1] + dp[i][j-1]

        arr = []
        for i in range(35):
            if (k >> i) & 1:
                arr.append(i)

        res = 0
        for i in range(length):
            cur, ans = i, i
            for idx in arr:
                ans += dp[cur][idx]
                cur = pos[cur][idx]
            res = max(res, ans)
        return res