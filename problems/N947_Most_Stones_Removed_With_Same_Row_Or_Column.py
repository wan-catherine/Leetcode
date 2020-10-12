import collections


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        length = len(stones)
        status = [-1]*length
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for index, li in enumerate(stones):
            i, j = li
            rows[i].append(index)
            cols[j].append(index)

        def dfs(i, f):
            if status[i] != -1:
                return
            status[i] = f
            for index in rows[stones[i][0]]:
                dfs(index, f)
            for index in cols[stones[i][1]]:
                dfs(index, f)

        for i in range(length):
            if status[i] == -1:
                dfs(i, i)

        count = collections.Counter(status)
        res = 0
        for k, v in count.items():
            if v < 2:
                continue
            res += v - 1
        return res