import collections


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S:
            return T
        counter = collections.Counter(T)
        res = []
        used = set(S)
        for c in S:
            if c in counter.keys():
                res.append(c*counter[c])
        for key, value in counter.items():
            if key not in used:
                res.append(key*value)
        return ''.join(res)
