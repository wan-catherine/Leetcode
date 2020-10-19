import collections


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        words = [['z','zero',0],['w', 'two', 2],['u','four',4], ['x','six',6], ['g', 'eight', 8],
                  ['o', 'one', 1],['s', 'seven', 7], ['f','five', 5], ['r', 'three', 3],
                 ['e', 'nine', 9]]

        res = []
        for c, word, n in words:
            if c in counter and counter[c] > 0:
                times = counter[c]
                res.extend([n]*times)
                for i in word:
                    counter[i] -= times
                    if counter[i] == 0:
                        del counter[i]
        res.sort()
        return ''.join([str(i) for i in res])
