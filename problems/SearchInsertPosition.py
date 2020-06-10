class Solution:
    def searchInsert_before(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if target <= nums[i]:
                break
            else:
                i += 1
        return i

    def searchInsert(self, nums, target):
        if not nums:
            return 0
        nums_len = len(nums)
        lo, hi = 0, nums_len
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return lo

