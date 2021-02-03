class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        arr = [0] * length
        for i in range(1, length):
            j = arr[i-1]
            while j > 0 and s[j] != s[i]:
                j = arr[j-1]
            if s[j] == s[i]:
                j += 1
            arr[i] = j
        return s[:arr[-1]]

