class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            for i in range(10):
                temp = cur*10 + i
                if temp > n:
                    return
                dfs(temp)
        for i in range(1, 10):
            dfs(i)
        return res