class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 2
        res = n - 1
        while i <= n // 2:
            j = n // i
            if n == i * j:
                temp = j ** i
            elif n == j * (i - 1) + j + 1:
                temp = j ** (i - 1) * (j + 1)
            elif n == (j + 1)*(i - 1) + j:
                temp = (j + 1) ** (i - 1) * j

            res = max(temp, res)
            i += 1
        return res