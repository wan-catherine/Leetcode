class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # n1 = int(num1)
        # n2 = int(num2)
        # return str(n1*n2)
        if num1 == "0" * len(num1) or num2 == "0" * len(num2):
            return "0"

        res = 0
        k = 1
        for ni in num2[::-1]:
            i = int(ni) * k
            for nj in num1[::-1]:
                j = int(nj)
                res += i * j
                i *= 10
            k *= 10
        return str(res)