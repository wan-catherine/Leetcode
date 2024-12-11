import collections
from typing import List


class Solution:
    def maximumBeauty_old(self, nums: List[int], k: int) -> int:
        arr = []
        for n in nums:
            arr.append((max(0, n - k), min(10**5,n + k )))
        arr.sort()
        count = [0] * (10**5 + 2)
        for s, e in arr:
            count[s] += 1
            count[e+1] -= 1
        res = 1
        current = 0
        for i in range(10**5 + 2):
            current += count[i]
            res = max(res, current)
        return res

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ct = collections.defaultdict(int)
        for n in nums:
            ct[n - k] += 1
            ct[n + k + 1] -= 1

        res = 0
        cur = 0
        for key in sorted(ct.keys()):
            cur += ct[key]
            res = max(res, cur)
        return res

