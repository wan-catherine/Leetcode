class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 2:
            return False

        res = True
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                continue
            if num % 3 == 0:
                num = num // 3
                continue
            if num % 5 == 0:
                num = num //5
                continue
            res = False
            break
        return res
