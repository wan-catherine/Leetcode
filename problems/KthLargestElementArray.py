import heapq

class Solution:
    def findKthLargest_before(self, nums, k):
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

    #use small heap
    # create a small heap with k lengh
    # then each time push one into the heap and pop the smallest one from the heap
    # at lates, the heap keeps the k-largest items
    # the first item is the smallest one in the k-largest items, so it's Kth largest item in the array
    def findKthLargest(self, nums, k):
        l = nums[:k]
        heapq.heapify(l)
        for n in nums[k:]:
            heapq.heappushpop(l, n)
        return l[0]
