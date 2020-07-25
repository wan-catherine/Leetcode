class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        sign = 1
        if numerator < 0:
            sign *= -1
            numerator = abs(numerator)
        if denominator < 0:
            sign *= -1
            denominator = abs(denominator)

        res = []
        if sign < 0:
            res.append('-')
        res.append(str(numerator // denominator))
        c = numerator % denominator
        if c == 0:
            return ''.join(res)
        else:
            res.append('.')

        count = {}
        while c and c not in count:
            count[c] = len(res)
            res.append(str(c*10 // denominator))
            c = c*10 % denominator

        if c == 0:
            return ''.join(res)
        else:
            res.insert(count[c], '(')
            res.append(')')
        return ''.join(res)




