class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        length = len(s)
        for i in range(length):
            res = res*26 + ord(s[i]) - ord('A') + 1
        return res