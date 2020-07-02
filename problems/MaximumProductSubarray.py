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
