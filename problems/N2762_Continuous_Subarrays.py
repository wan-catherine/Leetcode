from collections import deque
from typing import List


class Solution:
    def continuousSubarrays(self, nums):
        dmax, dmin = deque(), deque()
        length = len(nums)
        l, r = 0, 0
        res = 0
        while r < length:
            while len(dmax) > 0 and nums[dmax[-1]] < nums[r]:
                dmax.pop()
            dmax.append(r)
            while len(dmin) > 0 and nums[dmin[-1]] > nums[r]:
                dmin.pop()
            dmin.append(r)

            while len(dmax) > 0 and len(dmin) > 0 and nums[dmax[0]] - nums[dmin[0]] > 2:
                l += 1
                while len(dmax) > 0 and dmax[0] < l:
                    dmax.popleft()
                while len(dmin) > 0 and dmin[0] < l:
                    dmin.popleft()
            res += r - l + 1
            r += 1
        return res

