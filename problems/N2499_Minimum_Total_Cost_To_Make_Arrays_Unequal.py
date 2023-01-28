import collections
from typing import List

"""
1. find all same pair, those pairs we need to do operation. so the minimum cost is sum of index of those pairs. 
2. to check if there are any pair is the major during the same pairs . 
    a. if not, then those pair can do exchange , then result will be the cost from #1 
    b. if yes, then we need other diff pair to do exchange
3. for other diff pair, both of them can't have the same num as the major pair
"""
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        count = collections.Counter()
        same = 0
        res = 0
        for i in range(length):
            if nums1[i] == nums2[i]:
                same += 1
                count[nums1[i]] += 1
                res += i

        maxc, maxv = 0, 0
        for v, c in count.items():
            if c > maxc:
                maxc = c
                maxv = v
        if maxc <= same - maxc:
            return res

        left = maxc - (same - maxc)
        for i in range(length):
            if nums1[i] == nums2[i]:
                continue
            if nums1[i] == maxv or nums2[i] == maxv:
                continue
            left -= 1
            res += i
            if left == 0:
                break
        return res if left == 0 else -1