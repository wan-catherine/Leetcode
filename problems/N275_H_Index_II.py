from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        l, r = 0, length - 1
        while l < r:
            mid = (r - l) // 2 + l
            if citations[mid] >= length - mid:
                r = mid
            else:
                l = mid + 1
        return min(length - l, citations[l])