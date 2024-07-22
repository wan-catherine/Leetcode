from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[0 for _ in range(k + 1)] for _ in range(length)]
        res = 1
        for i in range(length):
            for t in range(k + 1):
                ans = 1
                for j in range(i):
                    if nums[i] == nums[j]:
                        ans = max(ans, dp[j][t] + 1)
                    elif t >= 1:
                        ans = max(ans, dp[j][t-1] + 1)
                dp[i][t] = ans
                res = max(res, ans)
        return res