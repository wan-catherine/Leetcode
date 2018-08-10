class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > -1 else -1
        positiveX = flag * x
        strX = str(positiveX)
        revsedX = strX[::-1]
        revsedIntX = int(revsedX) * flag

        if revsedIntX < -2 ** 31 or revsedIntX > 2 ** 31 -1 :
            revsedIntX = 0
        return revsedIntX


