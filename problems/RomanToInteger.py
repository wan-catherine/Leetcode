class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictSymbolValue = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90
            , "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
        if len(s) == 0:
            return  0
        elif len(s) == 1:
            return dictSymbolValue[s]
        i = 1
        res = 0
        while i < len(s):
            if dictSymbolValue[s[i]] <= dictSymbolValue[s[i - 1]]:
                res += dictSymbolValue[s[i - 1]]
                if i + 1 == len(s):
                    res += dictSymbolValue[s[i]]
                i += 1
            else:
                res += dictSymbolValue[s[i -1] + s[i]]
                if i + 2 == len(s):
                    res += dictSymbolValue[s[i + 1]]
                i += 2

        return res