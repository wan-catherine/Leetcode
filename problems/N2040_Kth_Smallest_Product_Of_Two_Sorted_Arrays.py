import bisect
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ll = len(nums2)
        def check(num):
            count = 0
            for n in nums1:
                if n > 0:
                    count += bisect.bisect(nums2, num / n)
                elif n < 0:
                    count += ll - bisect.bisect_left(nums2, num / n)
                elif num >= 0:
                    count += ll
            return True if count >= k else False

        l, r = - 10 ** 10 - 1, 10 ** 10 + 1
        while l < r:
            m = (r - l) // 2 + l
            # if helper(m):
            if check(m):
                r = m
            else:
                l = m + 1
        return l