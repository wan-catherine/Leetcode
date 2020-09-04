import collections
import itertools

"""
Two cases here : 
    1.  one block 
    2.  left block + x + right block

"""

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        a = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        count = collections.Counter(text)
        res = max(min(k+1, count[c]) for c, k in a)
        for i in range(1, len(a) - 1):
            if a[i-1][0] == a[i+1][0] and a[i][1] == 1:
                res = max(res, min(a[i+1][1] + a[i-1][1] + 1, count[a[i+1][0]]))
        return res