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
                # key point : status[j][diff] , not status[i][diff]
                # status[i][diff] we need to solove the [x,y] which is less than three issue.
                # but status[j][diff] we can know it will be >= 3.
                res += status[j][diff]
        return res
