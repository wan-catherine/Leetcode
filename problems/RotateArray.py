class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return
        l = k % len(nums)

        if l == 0:
            return

        # newNums = nums[-1 * l :] + nums[0:len(nums) - l]
        # nums.clear()
        # nums.extend(newNums)
        nums[:] = nums[-1 * l :] + nums[0:len(nums) - l]
