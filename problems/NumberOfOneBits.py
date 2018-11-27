class Solution(object):
    def hammingWeight(self, n):
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