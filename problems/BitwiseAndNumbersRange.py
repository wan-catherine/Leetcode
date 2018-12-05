class Solution:
    def rangeBitwiseAnd_slow(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        while m <= n:
            res &= m
            m += 1
        return res

    def rangeBitwiseAnd(self, m, n):
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        m <<= i
        return m

