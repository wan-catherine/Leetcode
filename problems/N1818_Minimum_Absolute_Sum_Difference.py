import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        length = len(nums1)
        arr = []
        total = 0
        for i in range(length):
            val = abs(nums1[i] - nums2[i])
            arr.append((val, i))
            total += val
        arr.sort(key=lambda x: x[0], reverse=True)
        snum = sorted(nums1)
        v = 0
        for diff, i in arr:
            if not diff:
                continue
            index = bisect.bisect_left(snum, nums2[i])
            if index == length or index > 0:
                new_diff = abs(snum[index-1] - nums2[i])
                if new_diff < diff:
                    v = max(v, diff - new_diff)
            if index < length:
                new_diff = abs(snum[index] - nums2[i])
                if new_diff < diff:
                    v = max(v, diff - new_diff)
        return (total - v) % (10**9 + 7)