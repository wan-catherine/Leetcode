import collections
import math
import sys
from typing import List


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        fmap = collections.defaultdict(int)
        for n in nums:
            fmap[n] += 1

        def helper(f):
            ans = 0
            for count in fmap.values():
                g = count // f
                d = count % f
                if d > g:
                    return sys.maxsize
                ans += math.ceil(count/(f + 1))
            return ans

        freq = min(fmap.values())
        res = len(nums)
        for f in range(1, freq + 1):
            res = min(res, helper(f))
        return res