class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in digits:
            res *= 10
            res += i

        res += 1
        num = []
        while res > 0:
            l = res % 10
            num.append(l)
            res = res//10

        num.reverse()
        return num