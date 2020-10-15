class Solution(object):
    def rotate_old(self, nums, k):
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
        nums[:] = nums[-1 * l :] + nums[0:len(nums) - l]

    def rotate(self, nums, k):
        length = len(nums)
        k = k % length

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, length - 1)
        reverse(0, k-1)
        reverse(k, length-1)