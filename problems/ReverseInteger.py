class Solution:
    def reverse2(self, x):
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

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > -1 else -1
        positiveX = flag * x
        res = 0
        while positiveX > 0:
            res = res * 10 + positiveX % 10
            positiveX = positiveX // 10

        res = res * flag
        if res < -2 ** 31 or res > 2 ** 31 -1 :
            res = 0

        return  res


