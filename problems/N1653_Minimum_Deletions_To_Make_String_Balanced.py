class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        a, b = [0] * (length + 1), [0] * (length + 1)
        for i in range(1, length+1):
            if s[i-1] == 'b':
                b[i] += 1
            b[i] += b[i-1]

        for i in range(length - 1, -1, -1):
            if s[i] == 'a':
                a[i] += 1
            a[i] += a[i+1]

        res = length
        for i in range(length):
            res = min(res, a[i] + b[i+1] - 1)
        return res