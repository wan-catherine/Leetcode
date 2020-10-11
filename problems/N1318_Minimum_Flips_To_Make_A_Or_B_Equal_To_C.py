class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            c_f = (1 << i) & c
            a_f = (1 << i) & a
            b_f = (1 << i) & b
            if not c_f:
                if a_f:
                    res += 1
                if b_f:
                    res += 1
            else:
                if not a_f and not b_f:
                    res += 1
        return res



