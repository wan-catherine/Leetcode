class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        total = sum(nums)
        if total <= threshold:
            return 1

        left, right = 0, max(nums)
        while left < right:
            mid = (right - left) // 2 + left
            temp = self.helper(mid, nums)
            if temp > threshold:
                left = mid + 1
            else:
                right = mid
        return left

    def helper(self, value, nums):
        res = 0
        for num in nums:
            if num % value:
                res += num // value + 1
            else:
                res += num // value
        return res