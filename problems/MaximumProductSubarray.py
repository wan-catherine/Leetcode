from math import inf


class Solution(object):
    def maxProduct_before(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res = 0
        last = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                res = max(res, self.helper(nums[last:i]))
                last = i + 1

        else:
            if last <= i:
                res = max(res, self.helper(nums[last:i+1]))
        return res


    def helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = 1
        first = None
        last = None
        for i in range(len(nums)):
            res *= nums[i]
            if nums[i] < 0:
                if first == None:
                    first = i
                last = i

        if res > 0:
            return res

        left = 1
        right = 1
        if first != None:
            for i in nums[0:first+1]:
                left *= i
        if last != None:
            for i in nums[last:]:
                right *= i

        return res/left if res/left > res/right else res/right

    """
    Detailed Explanation:
    A lot of people asked about why can we get the max by calculating the products from start and end, Here is all you should know:
    First, Consider there is no zero, and if we get the products of all the numbers:
    1) We will have a negative result if there are odd numbers of negative -> max ((product of (0, last negative)), (product of (first negative, last num))
    2) We will have a positive result if there are even numbers of negative -> product of all the numbers
    Above all, we can get the max by going through the array from both start and end, then we won't miss any situations
    If there is a zero, that means we would have two subproblems(unless the zero is at index 0 or last index), if two zeros, 3 subs, all the way up. We still can calculate from the very beginning and end at the same time, then we would get the result.


    the maximum product must either include the first element or end with the last element.
    1. all positive integer or has even number of negative integer, then include both first and end
    2. has odd number of negative integer, so either the include the first element or include the end element
    3. for zero, keep it
    """
    def maxProduct(self, nums):
        prefix = nums
        suffix = nums[::-1]
        for i in range(1, len(nums)):
            prefix[i] *= (prefix[i-1] or 1)
            suffix[i] *= (suffix[i-1] or 1)
        return max(prefix+suffix)
