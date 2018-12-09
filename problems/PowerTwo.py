class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n > 1:
            n /= 2

        if n == 0 or n == 1:
            return True
        else:
            return False