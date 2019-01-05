class Solution:
    def bulbSwitch_timeout(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 1:
            return 0
        if n == 1:
            return n
        l = [1] * (n+1)
        i = 2
        while i <= n:
            index = 1
            temp = index * i
            while temp  <= n:
                # l[temp] = 1 if l[temp] == 0 else l[temp] = 0
                if l[temp] == 0:
                    l[temp] = 1
                else:
                    l[temp] = 0
                index += 1
                temp = index * i
            i += 1

        return sum(l) - 1

    def bulbSwitch(self, n):
        import math
        return int(math.sqrt(n))