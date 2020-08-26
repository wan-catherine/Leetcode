class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        if not S:
            return res
        self.s = S
        for word in words:
            if self.check(word):
                res += 1
        return res

    def check(self, word):
        s1, s2, w1, w2 = [0] * 4
        n, m = len(word), len(self.s)
        while True:
            while s2 < m and self.s[s2] == self.s[s1]:
                s2 += 1

            while w2 < n and word[w2] == word[w1]:
                w2 += 1

            if self.s[s1:s2] == word[w1:w2]:
                s1 = s2
                w1 = w2
            elif self.s[s1] != word[w1] or s2 - s1 < w2 - w1 or s2 - s1 < 3:
                return False
            else:
                s1 = s2
                w1 = w2
            if s2 == m or w2 == n:
                break
        if s2 < m or w2 < n:
            return False
        return True

