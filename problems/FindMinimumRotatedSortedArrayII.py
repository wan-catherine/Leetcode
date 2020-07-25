class Solution(object):
    def findMin_before(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        i = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                return nums[i]
            i += 1
        return nums[-1]

    def findMin(self, nums):
        length = len(nums)

        left, right = 0, length - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]