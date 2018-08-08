class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        max = 0
        i = 0

        for j in range(1, len(s)):
            for k in range(i, j + 1):
                if s[k] == s[j] or k == j:
                    if k == j:
                        length = j - i + 1
                    else:
                        length = j - i
                        i = k + 1
                    if length > max:
                        max = length
                    break
        return max