import collections
from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[0 for _ in range(k + 1)] for _ in range(length)]
        max_all = [0] * (k + 1)
        max_value =[collections.defaultdict(int) for _ in range(k + 1)]
        res = 1
        for i in range(length):
            for t in range(k + 1):
                ans = 1
                if t >= 1:
                    ans = max(ans, max_all[t-1] + 1)
                ans = max(ans, max_value[t][nums[i]] + 1)
                dp[i][t] = ans
                res = max(res, ans)
            for it in range(k + 1):
                max_all[it] = max(max_all[it], dp[i][it])
                max_value[it][nums[i]] = max(max_value[it][nums[i]], dp[i][it])
        return res