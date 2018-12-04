class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = []
        return self.helper(n, nums)

    def helper(self, n, nums):
        res = 0
        while n > 0:
            temp = n % 10
            res += temp * temp
            n //= 10

        if res == 1:
            return True
        if res in nums:
            return False
        nums.append(res)
        return self.helper(res, nums)
