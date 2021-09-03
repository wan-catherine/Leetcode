from typing import List
"""
1060. Missing Element in Sorted Array
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Constraints:
    1 <= nums.length <= 5 * 104
    1 <= nums[i] <= 107
    nums is sorted in ascending order, and all the elements are unique.
    1 <= k <= 108

Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?
"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        length = len(nums)
        missing = nums[-1] - nums[0] + 1 - length
        if missing < k:
            return nums[-1] + k - missing

        l, r = 0, length
        while l < r:
            m = (r - l) // 2 + l
            v = nums[m] - nums[0] - m
            if v >= k:
                r = m
            else:
                l = m + 1
        # here nums[l] should be the smallest number which satifised missing number is k .
        # so we use nums[l-1] because the while l < r ends at l >= r 
        return nums[l-1] + k - (nums[l-1] - nums[0] - l + 1) # Need to minus the number of missing number from nums[l-1] to nums[0]