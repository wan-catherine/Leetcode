class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {"a":1, "e":1, "i":1, "o":1, "u":1}
        if n == 1:
            return 5

        for i in range(2, n+1):
            num = sum(d.values())
            val = 0
            for c in ["a","e","i","o","u"]:
                t = d[c]
                d[c] = num - val
                val += t
        return sum(d.values())

