import bisect
import collections
import sys
from typing import List


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = [set() for _ in range(101)]
        mapping = collections.defaultdict(list)
        for i, n in enumerate(nums):
            arr[n].add(i)
            mapping[n].append(i)
        res = []
        for l, r in queries:
            cur = -1
            ans = sys.maxsize
            for i in range(1, 101):
                if not mapping[i] or mapping[i][0] > r or mapping[i][-1] < l:
                    continue
                if l not in arr[i] and r not in arr[i]:
                    ld, rd = bisect.bisect_left(mapping[i], l), bisect.bisect_left(mapping[i], r)
                    if ld == rd:
                        continue
                if cur > 0 and cur != i:
                    ans = min(ans, i - cur)
                cur = i
            res.append(ans if ans != sys.maxsize else -1)
        return res


