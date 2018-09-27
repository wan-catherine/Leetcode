class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k < 1:
            return None

        res = [[] for i in range(k)]
        for i in range(1, n + 1):
            res[0].append([i])

        for i in range(1,k):
            for l in res[i - 1]:
                if l[i-1] == n:
                    continue
                for j in range(l[i - 1] + 1, n + 1):
                    lcopy = l.copy()
                    lcopy.append(j)
                    res[i].append(lcopy)
        return res[k - 1]
