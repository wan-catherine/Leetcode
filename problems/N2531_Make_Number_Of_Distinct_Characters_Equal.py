import collections
import string


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cf, cs = collections.Counter(word1), collections.Counter(word2)
        for f in cf.keys():
            for s in cs.keys():
                lf, ls = len(cf), len(cs)
                if f == s:
                    if lf == ls:
                        return True
                else:
                    if f not in cs:
                        ls += 1
                    if cf[f] == 1:
                        lf -= 1
                    if s not in cf:
                        lf += 1
                    if cs[s] == 1:
                        ls -= 1
                    if lf == ls:
                        return True
        return False









