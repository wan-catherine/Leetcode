"""
There should be some aabaab, then ababab
a - 2(x+1) = b - x
==> x = a - b - 2, so it means we can have x times b . aabaabaab....baa. then other are bababa
"""
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == 0 and B == 0:
            return ''
        if A == 0:
            return 'b'*B
        if B == 0:
            return 'a'*A

        if A > B:
            return self.helper(A, B, 'a', 'b')
        else:
            return self.helper(B, A, 'b', 'a')

    def helper(self, large, small, l, s):
        res = []
        val = large - small - 2
        if val > 0:
            res.append(2*l)
            for i in range(val):
                res.append(s+l*2)
            left = small - val
            for i in range(left):
                res.append(s+l)
        else:
            for i in range(small):
                res.append(l+s)
            res.append(l*(large-small))
        return ''.join(res)