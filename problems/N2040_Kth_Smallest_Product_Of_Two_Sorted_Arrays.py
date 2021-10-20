import bisect
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ii = bisect.bisect_left(nums1, 0)
        jj = bisect.bisect_left(nums2, 0)
        onen, onep, twon, twop = nums1[:ii], nums1[ii:], nums2[:jj], nums2[jj:]
        negative = len(onen) * len(twop) + len(onep) * len(twon)
        # use the four arrays , TLE!!!
        def helper(num):
            count = 0
            if num >= 0:
                count += negative
                for n in onep:
                    if n == 0:
                        count += len(twop)
                        continue
                    val = num / n
                    index = bisect.bisect(twop, val)
                    count += index
                for n in onen:
                    val = num / n
                    index = bisect.bisect_left(twon, val)
                    count += len(twon) - index
            else:
                for n in onen:
                    val = num / n
                    index = bisect.bisect_left(twop, val)
                    count += len(twop) - index
                for n in onep:
                    if n == 0:
                        continue
                    val = num / n
                    index = bisect.bisect(twon, val)
                    count += index
            if count >= k:
                return True
            return False
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
            if check(m)
                r = m
            else:
                l = m + 1
        return l