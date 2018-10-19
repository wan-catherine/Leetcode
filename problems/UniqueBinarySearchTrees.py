class Solution:
    def numTrees(self, n):
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
