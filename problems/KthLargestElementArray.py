class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quicksort(nums, 0, len(nums)-1)
        return nums[-1 * k]


    def quicksort(self, nums, start, end):
        if start < end:
            p = self.partition(nums, start, end)
            self.quicksort(nums, start, p - 1)
            self.quicksort(nums, p+1, end)

    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        for j in range(start,end):
            if nums[j] < pivot:
                if i != j:
                    nums[i],nums[j] = nums[j],nums[i]
                i+=1

        nums[i],nums[end] = nums[end],nums[i]
        return i
