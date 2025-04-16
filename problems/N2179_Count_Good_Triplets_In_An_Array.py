import bisect
from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        ph = {}
        for i in range(length):
            ph[nums1[i]] = i
        for i in range(length):
            nums2[i] = ph[nums2[i]]

        less = [0] * length
        more = [0] * length
        def helper():
            left = [nums2[0]]
            for i in range(1, length):
                idx = bisect.bisect_left(left, nums2[i])
                bisect.insort_left(left, nums2[i])
                less[i] = idx

            right = [nums2[-1]]
            for i in range(length-2, -1, -1):
                idx = bisect.bisect_left(right, nums2[i])
                more[i] = len(right) - idx
                bisect.insort_left(right, nums2[i])
        helper()
        res = 0
        for i in range(1, length - 1):
            res += less[i] * more[i]
        return res
