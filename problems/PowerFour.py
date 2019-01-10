class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False

        if num == 1:
            return True

        i = 4
        while i <= num:
            if i == num:
                return True
            i *= 4
        return False
