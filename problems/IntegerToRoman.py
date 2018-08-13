class Solution:
    def intToRoman_first(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        n = 0
        while num > 0:
            if num >= 1000:
                n = num // 1000
                num = num % 1000
                res += "M" * n
            elif num >= 900:
                res += "CM"
                num -= 900
            elif num >= 500:
                n = (num - 500) // 100
                num -= 500
                res += "D"
            elif num >= 400:
                res += "CD"
                num -= 400
            elif num >= 100:
                n = num // 100
                num = num % 100
                res += "C" * n
            elif num >= 90:
                res += "XC"
                num -= 90
            elif num >= 50:
                num -= 50
                res += "L"
            elif num >= 40:
                res += "XL"
                num -= 40
            elif num >= 10:
                n = num // 10
                num = num % 10
                res += "X" * n
            elif num >= 9:
                res += "IX"
                num = 0
            elif num >= 5:
                n = num - 5
                res += "V" + "I" * n
                num = 0
            elif num == 4:
                res += "IV"
                num = 0
            elif num < 4:
                res += "I" * num
                num = 0
        return  res

    def intToRoman(self, num):
        dictValueSymbol = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC"
            , 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for i in values:
            n = num // i
            if n == 0:
                continue
            res += n * dictValueSymbol[i]
            num = num % i
        return  res