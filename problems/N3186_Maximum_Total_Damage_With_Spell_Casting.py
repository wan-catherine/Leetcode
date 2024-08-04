import collections
from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ct = collections.Counter(power)
        li = sorted(ct.keys())
        length = len(li)
        dp = [0] * length
        dp[0] = ct[li[0]] * li[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1], ct[li[i]] * li[i])
            if i - 1 >= 0 and li[i] - li[i-1] > 2:
                dp[i] = max(dp[i], dp[i - 1] + ct[li[i]] * li[i])
            elif i - 2 >= 0 and li[i] - li[i - 2] > 2:
                dp[i] = max(dp[i], dp[i - 2] + ct[li[i]] * li[i])
            elif i - 3 >= 0:
                dp[i] = max(dp[i], dp[i - 3] + ct[li[i]] * li[i])
        return dp[-1]