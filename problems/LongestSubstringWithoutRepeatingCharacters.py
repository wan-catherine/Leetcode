class Solution:
    def lengthOfLongestSubstring_old(self, s):
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

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        s_len = len(s)
        i,j = 0,0
        window = {}
        res = 0
        while j < s_len:
            c = s[j]
            if c in window:
                res = max(res, len(window))
                index = window[c]
                while i < index + 1:
                    del window[s[i]]
                    i += 1
            if c not in window:
                window[c] = j
            j += 1

        return max(res, len(window))


