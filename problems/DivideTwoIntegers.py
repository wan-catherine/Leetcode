class Solution:
    def divide_before(self, dividend, divisor):
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

    def divide(self, dividend: int, divisor: int) -> int:
        def helper(a, b):
            if a < b:
                return 0
            count = 1
            val = b
            while val + val <= a:
                count += count
                val += val
            return count + helper(a - val, b)
        if dividend == 0:
            return 0
        if divisor == 1:
            if dividend < -2**31 or dividend > 2**31 - 1:
                return 2**31 - 1
            else:
                return dividend
        elif divisor == -1:
            if dividend <= -2**31 or dividend > 2**31:
                return 2**31 - 1
            else:
                return -dividend
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            val = helper(abs(dividend), abs(divisor))
        else:
            val = -helper(abs(dividend), abs(divisor))
        if val < -2 ** 31 or val > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return val
