import collections


class Solution(object):
    def removeStones_dfs(self, stones):
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

    def removeStones_union_find_list(self, stones):
        parent = list(range(20000))
        size = [1] * 20000

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            sx, sy = size[px], size[py]
            if sx > sy:
                parent[py] = px
                size[px] += size[py]
            else:
                parent[px] = py
                size[py] += size[px]

        for i, j in stones:
            union(i, j + 10000)

        group = collections.defaultdict(int)
        for i in parent:
            group[find(i)] += 1
        res = 0
        for i, v in group.items():
            if v >= 2:
                res += 1
        return len(stones) - res

    def removeStones(self, stones):
        uf = {}
