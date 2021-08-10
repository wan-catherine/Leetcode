import collections
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        status = [collections.defaultdict(int) for _ in range(length)]
        res = 0
        for i in range(1, length):
            for j in range(i):
                diff = nums[i] - nums[j]
                status[i][diff] += status[j][diff] + 1
                res += status[j][diff]
        return res
