import collections
import math
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        status = collections.defaultdict(int)
        length = len(nums)
        res = 1
        for i in range(length):
            v = int(math.sqrt(nums[i]))
            if v * v == nums[i]:
                status[nums[i]] = status[v] + 1
                res = max(res, status[nums[i]])
            else:
                status[nums[i]] = 1
        return res if res > 1 else -1