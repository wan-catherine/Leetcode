class Solution(object):
    def numSub_two_pointers(self, s):
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

    def numSub(self, s):
        arr = s.split('0')
        res = 0
        for li in arr:
            length = len(li)
            res += (1+length)*length//2
        return res % (10**9 + 7)

