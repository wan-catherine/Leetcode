import collections
from typing import List


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        length = len(nums)
        last = collections.defaultdict(int)
        for i, n in enumerate(nums):
            last[n] = i

        count = 0
        i = 0
        far = last[nums[i]]
        while i < length:
            if i < far:
                far = max(far, last[nums[i]])
                i += 1
            else:
                count += 1
                i += 1
                if i < length:
                    far = last[nums[i]]
        return 2 ** (count - 1) % M


