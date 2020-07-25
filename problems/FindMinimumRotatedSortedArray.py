class Solution(object):
    def findMin_before(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) < 1:
            return None

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                return nums[i]
            i += 1

    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]