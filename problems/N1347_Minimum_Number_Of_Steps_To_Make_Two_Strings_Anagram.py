import collections


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == t:
            return 0
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        if s_count == t_count:
            return 0
        res = 0
        for key in t_count:
            if key in s_count:
                t_count[key] = t_count[key] - s_count[key] if t_count[key] >= s_count[key] else 0
            res += t_count[key]
        return res
