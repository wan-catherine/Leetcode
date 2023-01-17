import collections
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        length = len(nums)
        ct = collections.defaultdict(int)
        count = 0
        res = 0
        l, r = 0, 0
        while r < length:
            ct[nums[r]] += 1
            count += (ct[nums[r]] - 1)
            if count >= k:
                res += length - r

                while l < r:
                    ct[nums[l]] -= 1
                    count -= ct[nums[l]]
                    l += 1
                    if count >= k:
                        res += length - r
                    else:
                        break

            r += 1
        return res