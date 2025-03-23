import collections
import heapq
from typing import List

"""
Greedy. 
decrease the larger one, and increase the smaller one
"""

class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2 :
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        diff, res = s2 - s1, 0
        count1, count2 = collections.Counter(nums1), collections.Counter(nums2)

        for val in range(5, 0, -1):
            while count1[6-val]:
                diff -= val
                count1[6 - val] -= 1
                res += 1
                if diff <= 0:
                    return res

            while count2[val + 1]:
                diff -= val
                count2[val+1] -= 1
                res += 1
                if diff <= 0:
                    return res
        return -1

    def minOperations_20250323(self, nums1: List[int], nums2: List[int]) -> int:
        lf, ls = len(nums1), len(nums2)
        if lf > ls * 6 or lf * 6 < ls:
            return -1
        t1, t2 = sum(nums1), sum(nums2)
        if t1 == t2:
            return 0
        if t1 < t2:
            return self.minOperations_20250323(nums2, nums1)
        first = [-n for n in nums1]
        heapq.heapify(first)
        heapq.heapify(nums2)
        diff = t1 - t2
        res = 0
        while diff > 0:
            f, s = -first[0] if first else 0, nums2[0] if nums2 else 0
            if f - 1 >= 6 - s:
                diff -= min(f - 1, diff)
                heapq.heappop(first)
            else:
                diff -= min(6 - s, diff)
                heapq.heappop(nums2)
            res += 1
        return res

