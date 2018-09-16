class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = [i for i in range(1, n+1)]
        res = ""

        for i in range(n-1, -1, -1):
            num = self.getNum(i)
            for j in range(1, n+1):
                if k <= j*num:
                    k -= (j - 1) * num
                    break
            p = 0
            for q in range(len(seq)):
                if seq[q] != 0:
                    p += 1
                if p == j:
                    res += str(seq[q])
                    seq[q] = 0
                    break
        return res

    def getNum(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res