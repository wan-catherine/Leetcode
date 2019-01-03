class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False

        if n == 1:
            return True

        i = 3
        while i <= n:
            if i == n:
                return True
            i *= 3
        return False
