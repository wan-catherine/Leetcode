import collections


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        length = len(s)
        if length < k:
            return False
        if length == k:
            return True

        counter = collections.Counter(s)
        odd = 0
        for key, value in counter.items():
            if value % 2:
                odd += 1
        if odd > k:
            return False
        return True
