class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        def partition(l, r):
            flag = l
            while l <= r:
                if nums[l] <= nums[flag]:
                    l += 1
                    continue
                if nums[r] >= nums[flag]:
                    r -= 1
                    continue
                nums[l], nums[r] = nums[r], nums[l]
            nums[flag], nums[r] = nums[r], nums[flag]
            return r

        def quicksort(left, right):
            if left >= right:
                return
            p = partition(left, right)
            quicksort(left, p-1)
            quicksort(p+1, right)

        quicksort(0, len(nums)-1)
        return nums



