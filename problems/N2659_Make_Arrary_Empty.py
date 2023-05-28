import collections
from typing import List
from others.BIT import BIT

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        length = len(nums)
        nums = [0] + nums
        bit = BIT(length)
        for i in range(1, length + 1):
            bit.update(i, 1)

        status = collections.defaultdict(int)
        for i in range(1, length + 1):
            status[nums[i]] = i

        keys = sorted(status.keys())
        last = -1
        res = length
        for key in keys:
            idx = status[key]
            if last == -1:
                res += bit.range(1, idx - 1)
            elif last < idx:
                res += bit.range(last, idx - 1)
            else:
                res += bit.range(1, idx - 1)
                res += bit.range(last, length)
            last = idx
            bit.update(idx, -1)
        return res

