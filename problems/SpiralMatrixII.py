class Solution:
    def generateMatrix_(self, n):
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

    def generateMatrix(self, n):
        table = [[0] * n for _ in range(n)]
        if n % 2:
            times = (n+1) // 2
        else:
            times = n//2

        k = 0
        for time in range(times):
            for col in range(time, n - time - 1):
                k += 1
                table[time][col] = k
                if k == n*n:
                    return table
            for row in range(time, n - time - 1):
                k += 1
                table[row][n - 1 - time] = k
                if k == n*n:
                    return table
            for col in range(n - 1 - time, time, -1):
                k += 1
                table[n - 1 - time][col] = k
                if k == n*n:
                    return table
            for row in range(n - 1 - time, time, -1):
                k += 1
                table[row][time] = k
                if k == n*n:
                    return table

        table[time][time] = k + 1
        return table