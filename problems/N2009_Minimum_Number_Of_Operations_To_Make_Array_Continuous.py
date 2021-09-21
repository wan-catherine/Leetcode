import bisect
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        snums = sorted(set(nums))
        ll = len(snums)
        if snums[0] + length - 1 >= snums[-1]:
            return length - ll
        maximum = 0
        for i in range(ll):
            index = bisect.bisect_left(snums, snums[i] + length - 1)
            if index == ll:
                maximum = max(maximum, index - i)
                break
            if snums[index] == snums[i] + length - 1:
                v = index - i + 1
            else:
                v = index - i
            if v > maximum:
                maximum = v
            if index == ll:
                break
        return length - maximum

