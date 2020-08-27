class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)
        start, end = 0, 0
        res = 0
        temp = 0
        vowel = 'aeiou'
        while end < length:
            if s[end] in vowel:
                temp += 1
            end += 1
            if end == length:
                res = max(res, temp)
                break
            if end - start == k:
                res = max(res, temp)
                if s[start] in vowel:
                    temp -= 1
                start += 1
        return res

