class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        strN = bin(n)[2:]
        if len(strN) < 32:
            strN = '0' * (32 - len(strN)) + strN
        return int(strN[::-1], 2)