class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = []
        while N:
            res.append(N & 1)
            N = -(N // 2)
        return "".join(map(str, res[::-1] or [0]))