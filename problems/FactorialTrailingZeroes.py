class Solution(object):
    def trailingZeroes_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        res = 1
        while i <= n:
            res *= i
            i += 1

        strres = str(res)
        i = len(strres) - 1
        count = 0
        while i >= 0:
            if strres[i] == "0":
                count += 1
                i -= 1
            else:
                break
        return count
