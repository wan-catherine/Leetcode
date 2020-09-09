class Solution(object):
    def countNumbersWithUniqueDigits_backtracing(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        self.marked = [0] * 10
        self.res = 0
        for i in range(10):
            self.marked[i] = 1 if i > 0 else 0
            if i == 0:
                self.res += self.dfs(n-1, False)
            else:
                self.res += self.dfs(n-1, True)
            self.marked[i] = 0
        return self.res

    def dfs(self, n, flag):
        if n <= 0:
            return 1
        res = 0
        for i in range(10):
            if flag:
                if self.marked[i]:
                    continue
                self.marked[i] = 1
                res += self.dfs(n-1, flag)
                self.marked[i] = 0
            else:
                if i != 0:
                    flag = True
                    self.marked[i] = 1
                    res += self.dfs(n-1, flag)
                    self.marked[i] = 0
                else:
                    res += self.dfs(n-1, flag)

        return res

    def countNumbersWithUniqueDigits(self, n):
        choices = [9] + [i for i in range(9, 0, -1)]
        res, temp = 1, 1
        for i in range(n):
            temp *= choices[i]
            res += temp
        return res