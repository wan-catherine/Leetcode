import bisect
from typing import List


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        res = 0
        while flowers and flowers[-1] >= target:
            res += full
            flowers.pop()

        if not flowers:
            return res

        length = len(flowers)
        presum = flowers[:]
        for i in range(1, length):
            presum[i] += presum[i-1]

        diff = []
        for i in range(length):
            diff.append((i + 1) * flowers[i] - presum[i])

        ans = 0
        for i in range(length - 1, -1, -1):
            if newFlowers < 0:
                break
            if presum[i] + newFlowers >= (target - 1) * (i + 1):
                ans = max(ans, (target - 1) * partial + (length - i - 1) * full)
            else:
                idx = bisect.bisect(diff, newFlowers)
                if idx == len(diff) or diff[idx] > newFlowers:
                    idx -= 1
                each = (presum[idx] + newFlowers) // (idx + 1)
                ans = max(ans, each * partial + (length - i - 1) * full)
            newFlowers -= target - flowers[i]
            diff.pop()

        if newFlowers >= 0:
            ans = max(ans, length * full)

        return res + ans