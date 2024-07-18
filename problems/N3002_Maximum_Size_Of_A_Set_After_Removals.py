from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        half = length // 2
        sf, ss = set(nums1), set(nums2)

        it = sf.intersection(ss)
        lsf, lss, lit = len(sf), len(ss), len(it)

        if lsf <= half and lss <= half:
            return lsf + lss - lit
        elif lsf <= half and lss > half:
            return lsf + lss - max(lit, lss - half)
        elif lsf > half and lss <= half:
            return lss + lsf - max(lit, lsf - half)
        else:
            return min(length, lsf + lss - lit)