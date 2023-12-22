import collections
from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        amounts = collections.defaultdict(int)
        for c in coins:
            amounts[c] += c
        cur, sum = 0, 0
        for i in range(1, target + 1):
            if i in amounts:
                sum += amounts[i]
            elif i > sum:
                cur += 1
                sum += i
        return cur

