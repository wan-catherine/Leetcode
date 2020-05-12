"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

If an array which all element appears exactly twice, it means :
    index is even : array[index] equals array[index+1]
    index is odd: array[index] equals array[index-1]

so here we can use binary search to make the time complexity is O(logn):

"""
class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if not nums:
            return nums
        if len(nums) == 1:
            return nums[0]

        i = 0
        j = len(nums)
        while i < j:
            mid = i + (j - i) // 2
            if mid == i:
                return nums[mid]
            if mid % 2:
                if nums[mid-1] == nums[mid]:
                    i = mid + 1
                elif nums[mid] == nums[mid+1]:
                    j = mid - 1
                else:
                    return nums[mid]
            else:
                if nums[mid+1] == nums[mid]:
                    i = mid + 2
                elif nums[mid] == nums[mid-1]:
                    j = mid -2
                else:
                    return nums[mid]
        return nums[i]



