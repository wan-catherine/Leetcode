class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        letters = [0] * 26
        for i in s:
            index = ord(i) - ord('a')
            if not letters[index]:
                letters[index] = 1

        return ''.join([chr(ord('a') + index) for index in range(26) if letters[index]])