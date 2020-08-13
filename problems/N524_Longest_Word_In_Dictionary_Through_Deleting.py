class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        self.length = len(s)
        longest = 0
        res = ''
        for word in d:
            word_len = len(word)
            if not self.check(s, word, word_len):
                continue
            if word_len < longest:
                continue
            if word_len == longest:
                res = word if word < res else res
            if word_len > longest:
                res = word
                longest = word_len

        return res

    def check(self, s, word, word_len):
        i, j = 0, 0

        while i < self.length and j < word_len:
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == word_len:
            return True
        else:
            False

