import bisect
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        length = len(nums1)
        arr = []
        for i in range(length):
            arr.append(nums1[i]-nums2[i])

        ans = []
        res = 0
        for i in range(length):
            index = bisect.bisect_left(ans, arr[i] + diff + 1)
            res += index
            bisect.insort(ans, arr[i])
        return res
