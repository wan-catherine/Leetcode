class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num - 9 * (int)((num-1)/9)