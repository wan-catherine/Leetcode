from typing import List


class Solution:
    def combine_2019(self, n, k):
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

    def combine(self, n, k):
        if k < 1:
            return None

        res = []
        nums = [i for i in range(1, n+1)]
        self.dfs(nums, k , [], res)
        return res

    def dfs(self, nums, k, temp, res):
        if k == 0:
            res.append(temp[:])
        for i in range(len(nums)):
            temp.append(nums[i])
            self.dfs(nums[i+1:] , k - 1, temp, res)
            temp.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(index, cur):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(index, n):
                cur.append(i + 1)
                dfs(i + 1, cur[:])
                cur.pop()

        dfs(0, [])
        return res