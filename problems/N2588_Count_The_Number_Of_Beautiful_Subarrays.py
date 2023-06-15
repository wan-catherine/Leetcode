import collections
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        mapping = collections.defaultdict(int)
        mapping[0] = 1
        xor = 0
        res = 0
        for n in nums:
            xor = xor ^ n
            res += mapping[xor]
            mapping[xor] += 1
        return res
