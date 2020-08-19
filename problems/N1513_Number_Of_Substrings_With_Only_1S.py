class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '0'
        length = len(s)
        start, end = -1, 0
        res = 0
        while end < length:
            if s[end] == "1":
                res += end - start
            else:
                start = end
            end += 1
        return res % (10 ** 9 + 7)

