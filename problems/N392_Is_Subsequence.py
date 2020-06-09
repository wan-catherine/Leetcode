class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        s_len = len(s)
        t_len = len(t)
        if s_len > t_len:
            return False

        j = 0
        for i in range(t_len):
            if j < s_len and t[i] == s[j]:
                j+=1
            if j == s_len:
                break
        if j == s_len:
            return True
        else:
            return False