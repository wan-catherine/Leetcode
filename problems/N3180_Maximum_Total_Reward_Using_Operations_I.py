from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        length = len(rewardValues)
        rewardValues.sort()
        dp = set()
        dp.add(0)
        dp.add(rewardValues[0])
        for i in range(1, length):
            ndp = set()
            for n in dp:
                if rewardValues[i] > n:
                    ndp.add(rewardValues[i] + n)
                ndp.add(n)
            dp = ndp
        return max(dp)


