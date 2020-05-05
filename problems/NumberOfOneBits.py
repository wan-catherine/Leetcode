class Solution(object):
    def hammingWeight_before(self, n):
        """
        :type n: int
        :rtype: int
        """
        strN = bin(n)[2:]
        count = 0
        for i in strN:
            if i == "1":
                count += 1
        return count

    def hammingWeight(self, n):
        result = 0
        mask = 1
        for i in range(32):
            if n & mask:
                result += 1
            mask <<= 1
        return result