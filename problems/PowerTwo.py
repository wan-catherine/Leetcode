"""
if a number is a power of two , then N & N-1 == 0
for example:
8&7 == 0
 1000
 0111
&0000
"""
class Solution:
    def isPowerOfTwo_before(self, n):
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

    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0