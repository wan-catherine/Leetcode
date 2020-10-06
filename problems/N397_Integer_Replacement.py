class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        while n != 1:
            if not n % 2:
                n //= 2
                res += 1
                continue
            # check if add 1 can reduce the number of '1', if yes, then add 1, if no, then minus 1.
            # notice , n > 3, if n == 3, minus 1 will be better.
            if n > 3 and n & 3 == 3:
                n += 1
            else:
                n -= 1
            res += 1
        return res