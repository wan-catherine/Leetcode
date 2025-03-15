import sys
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[0,0] for _ in range(length)]
        def check(m) :
            dp[0][0] = 0
            if nums[0] <= m:
                dp[0][1] = 1
            else:
                dp[0][1] = -sys.maxsize

            for i in range(1,length):
                if nums[i] > m:
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = -sys.maxsize
                else:
                    dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = dp[i-1][0] + 1
            return max(dp[-1][1],dp[-1][0]) >= k

        l, r = 0, 10 ** 9 + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l