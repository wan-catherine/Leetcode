class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]]

        res = []
        for i in range(n):
            res.append([0]*n)

        self.oneCycle(res, n, 0, 1)

        return res

    def oneCycle(self, res, n, round, num):
        if n <= 0:
            return

        if n == 1:
            res[round][round] = num
            return

        for i in range(n):
            res[round][i + round] = num
            num += 1

        for j in range(1, n - 1):
            res[j + round][n - 1 + round] = num
            num += 1

        for k in range(n - 1, -1, -1):
            res[n - 1 + round][k + round] = num
            num += 1

        for v in range(n - 2, 0, -1):
            res[v + round][round] = num
            num += 1

        round += 1
        n -= 2
        self.oneCycle(res, n, round, num)