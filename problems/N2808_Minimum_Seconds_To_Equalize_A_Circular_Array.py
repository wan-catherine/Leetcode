import collections
from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        length = len(nums)
        first = {}
        prev = {}
        mapping = collections.defaultdict(list)
        for i, n in enumerate(nums):
            if n not in first:
                first[n] = i
                prev[n] = i
            else:
                mapping[n].append(i - prev[n] - 1)
                prev[n] = i
        for n in first.keys():
            mapping[n].append(length - prev[n] - 1 + first[n])
        res = length - 1
        for n, li in mapping.items():
            cur = 0
            for l in li:
                cur = max(cur, (l + 1) // 2)
            res = min(res, cur)
        return res


