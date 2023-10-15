import bisect
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        length = len(nums)
        arr = []
        for i in range(indexDifference, length):
            bisect.insort(arr, (nums[i-indexDifference], i-indexDifference))
            if abs(nums[i] - arr[0][0]) >= valueDifference:
                return [arr[0][1], i]
            if abs(nums[i] - arr[-1][0]) >= valueDifference:
                return [arr[-1][1], i]
        return [-1, -1]
