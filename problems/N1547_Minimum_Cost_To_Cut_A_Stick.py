from math import inf


class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        self.cuts = sorted(cuts)
        self.dp = {}

        res = self.calculate(0, n)
        print(self.dp)
        return res

    def  calculate(self, i, j):
        if (i,j) in self.dp:
            return self.dp[(i,j)]

        self.dp[(i, j)] = inf
        for cut in self.cuts:
            if cut <= i or cut >= j:
                continue
            self.dp[(i,j)] = min(self.dp[(i,j)], self.calculate(i, cut)+self.calculate(cut, j) + j - i)
        #This is the key part . For those stick : [i,j], which doesn't have any cut , so the cost is zeor!!!
        if self.dp[(i, j)] == inf :
            self.dp[(i, j)] = 0
        return self.dp[(i,j)]

