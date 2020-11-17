import collections


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        if set(c1.keys()).difference(set(c2.keys())):
            return False

        l1 = sorted(c1.values())
        l2 = sorted(c2.values())

        if l1 != l2:
            return False

        return True
