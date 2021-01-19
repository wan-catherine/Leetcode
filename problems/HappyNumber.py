class Solution:
    def isHappy_(self, n):
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

    """
    Space : O(1), 
    Use fast-slow pointer to test the cycle 
    """
    def isHappy(self, n):
        def check(i):
            s = 0
            while i:
                t = i % 10
                s += t * t
                i //= 10
            return s

        slow, fast = n, n
        while True:
            slow = check(slow)
            fast = check(fast)
            fast = check(fast)
            print(slow, fast)
            if slow == fast:
                break
        if slow == 1:
            return True
        return False
