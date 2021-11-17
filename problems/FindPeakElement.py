from typing import List


class Solution(object):
    def findPeakElement_linear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return None
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0

        i = 1
        while i < len(nums) - 1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i += 1
        if nums[i] > nums[i-1]:
            return i

    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1

        l, r = 1, length - 1
        while l < r:
            mid = (r - l) // 2 + l
            if mid > 0 and nums[mid] > nums[mid-1] and mid < length - 1 and nums[mid] > nums[mid + 1]:
                return mid
            if mid > 1 and nums[mid] < nums[mid-1]:
                r = mid
            elif mid < length - 1 and nums[mid] < nums[mid+1]:
                l = mid + 1

    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1
        l, r = 0, length
        while l < r:
            mid = (r - l) // 2 + l
            if mid + 1 < length:
                if nums[mid] < nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
            elif mid - 1 >= 0:
                if nums[mid] < nums[mid - 1]:
                    r = mid
                else:
                    l = mid - 1
        return l