class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) < 1:
            return 0
        s = s.rstrip()
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            res += 1

        return res
