from collections import defaultdict
from math import inf

"""
This problem is actually ask to get the greatest common divisor. 
"""
class Solution(object):
    def hasGroupsSizeX_slow(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck:
            return False

        deck_len = len(deck)
        if deck_len < 2:
            return False

        dict = defaultdict(int)
        for i in deck:
            dict[i] += 1
        min_num = min(dict.values())

        x = 2
        while x <= min_num:
            flag = True
            for key in dict:
                if dict[key] % x:
                    flag = False
                    break
            if flag:
                return flag
            x += 1
        return False

    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if not deck:
            return False

        deck_len = len(deck)
        if deck_len < 2:
            return False

        dict = defaultdict(int)
        for i in deck:
            dict[i] += 1

        x = float(inf)
        keys = list(dict.keys())
        for i in range(1, len(keys)):
            x = min(x, gcd(dict[keys[i]], dict[keys[i-1]]))
        if x >= 2:
            return True
        else:
            return False
