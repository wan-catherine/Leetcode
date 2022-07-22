from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        l, r = 0, length - 1
        while l < r:
            mid = (r - l + 1) // 2 + l
            if mid > 0:
                if arr[mid] > arr[mid-1]:
                    l = mid
                else:
                    r = mid - 1
            else:
                return mid
        return l
