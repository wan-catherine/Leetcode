class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positiveDividend = dividend if dividend > 0 else dividend * -1
        positiveDivisor = divisor if divisor > 0 else divisor * -1

        left = positiveDividend
        count = 0
        while left >= positiveDivisor:
            i = 0
            temp = positiveDivisor
            while temp <= left:
                temp = temp << 1
                i += 1
            left -= temp >> 1
            count += 2 ** (i - 1)
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0):
            if count > 2**31 - 1:
                return 2**31 -1
            else:
                return count
        else:
            if count < -2 ** 31:
                return -2 ** 31
            else:
                return  count * -1
