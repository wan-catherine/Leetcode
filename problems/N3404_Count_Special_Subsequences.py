import bisect
import collections
import math
from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        length = len(nums)
        def getKey(a, b):
            gcd = math.gcd(a, b)
            a = a // gcd
            b = b // gcd
            return a * 1000 + b

        ct = collections.defaultdict(list)
        for i in range(length):
            for j in range(i + 2, length):
                bisect.insort_left(ct[getKey(nums[i], nums[j])], i)

        res = 0
        for i in range(length):
            for j in range(i + 2, length):
                key = getKey(nums[j], nums[i])
                idx = bisect.bisect_left(ct[key], j + 2)
                res += len(ct[key]) - idx
        return res