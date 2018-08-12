import string
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digits = []
        for i in str:
            if len(digits) == 0 and i == ' ':
                continue
            elif (len(digits) == 0 and i in "-+") or i in string.digits:
                digits.append(i)
            else:
                break
        num = ''.join(digits)
        if num == '' or (len(num) == 1 and num in "-+"):
            return 0
        else:
            num = int(num)
        if num > 2 ** 31 -1:
            return 2 ** 31 - 1
        elif num < -2 ** 31:
            return -2 ** 31
        else:
            return num
