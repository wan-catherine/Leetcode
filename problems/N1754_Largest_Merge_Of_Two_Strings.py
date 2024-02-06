"""
When both are equal , should choose the next character from the larger string.
"""
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        lf, ls = len(word1), len(word2)
        res = []
        i, j = 0, 0
        while i < lf and j < ls:
            if word1[i] > word2[j]:
                res.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                res.append(word2[j])
                j += 1
            else:
                if word1[i:] >= word2[j:]:
                    res.append(word1[i])
                    i += 1
                else:
                    res.append(word2[j])
                    j += 1

        if i < lf:
            res.append(word1[i:])
        if j < ls:
            res.append(word2[j:])
        return ''.join(res)