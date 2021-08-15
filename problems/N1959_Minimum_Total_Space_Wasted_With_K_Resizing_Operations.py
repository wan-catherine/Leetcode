import sys
from typing import List


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[sys.maxsize] * (k + 1) for _ in range(length)]
        total, mx = 0, 0
        for i in range(length):
            mx = max(mx, nums[i])
            total += nums[i]
            dp[i][0] = mx * (i + 1) - total
        for i in range(1, length):
            for j in range(1, min(i, k) + 1):
                cur, mx = 0, 0
                for p in range(i, max(j-1,1)-1, -1):
                    mx = max(mx, nums[p])
                    cur += nums[p]
                    dp[i][j] = min(dp[i][j], dp[p-1][j-1] + mx * (i - p + 1) - cur)
        res = sys.maxsize
        for i in range(k + 1):
            res = min(res, dp[-1][i])
        return res
