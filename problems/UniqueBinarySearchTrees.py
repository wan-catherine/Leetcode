class Solution:
    def numTrees_before(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1,1,2]

        if n < 3:
            return n

        i = 3
        while i <= n:
            count = 0
            for j in range(1,i+1):
                count += res[j-1]*res[i-j]
            res.append(count)
            i += 1
        return res[n]

    def numTrees(self, n):
        res = [0]*(n+1)
        res[0] = 1
        for i in range(1,n+1):
            for j in range(1,i+1):
                res[i] += res[i-j] * res[j-1]
        return res[n]
