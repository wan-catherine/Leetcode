from typing import List


class Solution:
    def maxTotalReward_bit(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        x = 1
        print(rewardValues)
        for n in rewardValues:
            vx = x & ((1 << n) - 1)
            print(vx)
            x |= vx << n
            # print(x)
        return x.bit_length() - 1

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        def helper(idx, rmax):
            print(idx, rmax)
            res = 0
            for i in reversed(range(idx)):
                if rewardValues[i] > rmax:
                    continue
                nrmax = min(rmax - rewardValues[i], rewardValues[i] - 1)
                if nrmax + rewardValues[i] <= res:
                    break
                res = max(res, rewardValues[i] + helper(i, nrmax))
            return res
        rewardValues = sorted(list(set(rewardValues)))
        length = len(rewardValues)
        return rewardValues[length - 1] + helper(length - 1, rewardValues[length - 1] - 1)
