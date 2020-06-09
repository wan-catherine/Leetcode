"""
For nums, in order to find the smallest positive integer,
we can know , normal nums should be 1,2,...,len(nums)
but now some integers are missing .
so we know :
    1.min(nums) == 1
    2.max(nums) == len(nums)

when we loop the array, we only consider 1 <= x <= len(nums), all other won't influence result.

Here is the magic of the arrary which value is nums[i] = i + 1.
we need to put the right number to their own position which is for nums[i] put in position : nums[i] - 1

first test nums[nums[i]-1] == nums[i]:
if it's true, it means the number in the right position.
if not , then swap them 
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 1

        for i in range(length):
            while (nums[i] > 0 and nums[i] <= length):
                j = nums[i] - 1
                if (nums[i] != nums[j]):
                    nums[i], nums[j] = nums[j],nums[i]
                else:
                    break

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1




