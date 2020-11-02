import collections


class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_t, len_s = len(t), len(s)
        sub_t = collections.defaultdict(int)
        for i in range(len_t):
            for j in range(i+1):
                sub_t[t[j:i+1]] += 1

        sub_s = collections.defaultdict(int)
        for i in range(len_s):
            for j in range(i + 1):
                sub_s[s[j:i + 1]] += 1
        res = 0
        count = collections.Counter(t)
        letters = count.keys()
        for w in sub_s:
            l = len(w)
            for i in letters:
                for j in range(l):
                    if w[j] == i:
                        continue
                    word = w[:j] + i + w[j+1:]
                    if word in sub_t:
                        res += sub_t[word] * sub_s[w]
        return res

