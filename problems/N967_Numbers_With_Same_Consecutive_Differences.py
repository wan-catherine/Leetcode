class Solution(object):
    def numsSameConsecDiff_iterate(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = [0,1,2,3,4,5,6,7,8,9]
        for i in range(1, N):
            temp = []
            for j in res:
                if j == 0:
                    continue
                val = j % 10
                if val + K < 10:
                    temp.append(j*10 + val + K)
                if K == 0:
                    continue
                if val - K >= 0:
                    temp.append(j*10 + val - K)
            res = temp
        return res

    def numsSameConsecDiff(self, N, K):
        res = []
        if N == 1:
            res.append(0)
        for i in range(1,10):
            self.dfs(N-1, K, res, i)
        return res

    def dfs(self, n, k, res, temp):
        if not n:
            res.append(temp)
            return

        val = temp % 10
        if val + k < 10:
            self.dfs(n-1, k, res, temp*10 + val + k)
        if k!= 0 and val - k >= 0:
            self.dfs(n-1, k, res, temp*10 + val - k)
        return


