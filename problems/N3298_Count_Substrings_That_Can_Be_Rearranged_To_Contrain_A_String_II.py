import collections


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ct = collections.Counter(word2)
        lt = len(ct)
        length = len(word1)

        j = 0
        cur = collections.Counter()
        count = 0
        res = 0
        for i in range(length):
            while j < length and count < lt:
                cur[word1[j]] += 1
                if word1[j] in ct and ct[word1[j]] == cur[word1[j]]:
                    count += 1
                j += 1
            if count == lt:
                res += length - j + 1
            if word1[i] in ct and ct[word1[i]] == cur[word1[i]]:
                count -= 1
            cur[word1[i]] -= 1
        return res
