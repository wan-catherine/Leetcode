import sys
from typing import List


class Solution:
    def findMedianSortedArrays_(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)

        i = 0
        j = 0
        res = []

        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        if i < len1:
            res.extend(nums1[i:])
        elif j < len2:
            res.extend(nums2[j:])

        index = (len1 + len2) // 2
        if (len1 + len2) % 2 != 0:
            median = res[index]
        else:
            median = (res[index - 1] + res[index]) / 2

        return median

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, m + 1
        while l < r:
            pm = (r - l) // 2 + l
            pn = (m + n + 1) // 2 - pm
            maxlm = nums1[pm - 1] if pm > 0 else -sys.maxsize
            minrm = nums1[pm] if pm < m else sys.maxsize

            maxln = nums2[pn - 1] if pn > 0 else -sys.maxsize
            minrn = nums2[pn] if pn < n else sys.maxsize

            if maxlm <= minrn and maxln <= minrm:
                if (m + n) % 2:
                    return max(maxlm, maxln)
                else:
                    return (max(maxlm, maxln) + min(minrn, minrm)) / 2
            elif maxlm > minrn:
                r = pm
            else:
                l = pm + 1


