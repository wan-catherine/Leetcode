class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        oldX = x
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10

        if res == oldX:
            return True
        else:
            return False