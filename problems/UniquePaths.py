class Solution:
    def uniquePaths_slow(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = []
        self.cursive(m,n,res)
        return len(res)


    def cursive(self, m, n, res):
        if m == 1 and n == 1:
            res.append(1)
        if m - 1 > 0:
            self.cursive(m - 1, n, res)
        if n - 1 > 0:
            self.cursive(m, n - 1, res)

    def uniquePaths(self, m, n):
        res = [[0] * m for i in range(n)]

        for i in range(m):
            res[0][i] = 1
        for i in range(n):
            res[i][0] = 1

        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i -1][j] + res[i][j - 1]


        return res[n - 1][m - 1]