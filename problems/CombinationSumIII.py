class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        self.backTracing(k, n, 1, res, [])
        return res

    def backTracing(selfs, k, n, start, res, temp):
        if k < 1:
            if n == 0:
                res.append(temp.copy())
            return

        for i in range(start,10):
            temp.append(i)
            selfs.backTracing(k-1, n-i, i+1, res, temp)
            temp.pop()
