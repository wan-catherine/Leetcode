import sys
from typing import List

"""
Can't believe it , it's a DP!!!
"""

class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        arr = [(0,0)]
        length = len(nums1)
        for i in range(length):
            arr.append((nums1[i], nums2[i]))
        arr.sort(key=lambda x: x[1])
        prex = []
        cur = 0
        for i in range(length + 1):
            cur += arr[i][1]
            prex.append(cur)
        dp = [[sys.maxsize] * (length + 1) for _ in range(length + 1)]
        dp[0][0] = 0
        for i in range(1, length + 1):
            for j in range(length + 1):
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + prex[i-1])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + arr[i][0] + arr[i][1] * j)
        res = sys.maxsize
        for i in range(length + 1):
            if dp[length][i] <= x:
                res = min(res, i)
        return res if res < sys.maxsize else -1