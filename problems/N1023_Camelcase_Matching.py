class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []
        for word in queries:
            if self.check(word, pattern):
                res.append(True)
            else:
                res.append(False)
        return res

    def check(self, word, pattern):
        i, j = 0, 0
        w_len, p_len = len(word), len(pattern)
        while i < w_len and j < p_len:
            if word[i] == pattern[j]:
                i += 1
                j += 1
            elif word[i] in "abcdefghijklmnopqrstuvwxyz":
                i += 1
            else:
                return False
        if j < p_len:
            return False
        for i in range(i, w_len):
            if word[i] not in "abcdefghijklmnopqrstuvwxyz":
                return False
        return True
