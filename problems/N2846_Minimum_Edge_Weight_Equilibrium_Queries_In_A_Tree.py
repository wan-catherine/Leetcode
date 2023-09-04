import collections
import math
from typing import List


class Solution:
    def minOperationsQueries_TLE(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        count = [[0] * 27 for _ in range(n)]
        parent = [0] * n

        level = [0] * n
        cur = [0] * 27
        def dfs(idx, p, l):
            for nxt, weight in graph[idx]:
                if nxt == p:
                    continue
                cur[weight] += 1
                parent[nxt] = idx
                level[nxt] = l + 1
                for i in range(1, 27):
                    count[nxt][i] = cur[i]
                dfs(nxt, idx, l + 1)
                cur[weight] -= 1
        dfs(0, -1, 0)
        def lca(a, b):
            while True:
                if level[a] < level[b]:
                    b = parent[b]
                elif level[a] > level[b]:
                    a = parent[a]
                elif a == b:
                    return a
                else:
                    a, b = parent[a], parent[b]
        res = []
        for u, v in queries:
            total, maximum, temp = 0, 0, [0] * 27
            for i in range(1, 27):
                temp[i] = count[u][i] + count[v][i] - 2 * count[lca(u, v)][i]
            for i in range(1, 27):
                total += temp[i]
                maximum = max(maximum, temp[i])
            res.append(total - maximum)
        return res

    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        count = [[0] * 27 for _ in range(n)]
        parent = [0] * n

        level = [0] * n
        cur = [0] * 27

        def dfs(idx, p, l):
            for nxt, weight in graph[idx]:
                if nxt == p:
                    continue
                cur[weight] += 1
                parent[nxt] = idx
                level[nxt] = l + 1
                for i in range(1, 27):
                    count[nxt][i] = cur[i]
                dfs(nxt, idx, l + 1)
                cur[weight] -= 1

        dfs(0, -1, 0)

        ancestor = [[0] * 18 for _ in range(n)]
        for i in range(n):
            ancestor[i][0] = parent[i]
        M = math.ceil(math.log(n) // math.log(2))
        for j in range(1, M + 1):
            for i in range(n):
                ancestor[i][j] = ancestor[ancestor[i][j-1]][j-1]

        def getKthAncestor(idx, k):
            cur = idx
            for j in range(18):
                if (k >> j) & 1:
                    cur = ancestor[cur][j]
            return cur

        def lca(a, b):
            if level[a] < level[b]:
                b = getKthAncestor(b, level[b] - level[a])
            elif level[a] > level[b]:
                a = getKthAncestor(a, level[a] - level[b])
            l, r = 0, level[a]
            while (l < r):
                mid = (r - l) // 2 + l
                if getKthAncestor(a, mid) == getKthAncestor(b, mid):
                    r = mid
                else:
                    l = mid + 1
            return getKthAncestor(a, l)

        res = []
        for u, v in queries:
            total, maximum, temp = 0, 0, [0] * 27
            for i in range(1, 27):
                temp[i] = count[u][i] + count[v][i] - 2 * count[lca(u, v)][i]
            for i in range(1, 27):
                total += temp[i]
                maximum = max(maximum, temp[i])
            res.append(total - maximum)
        return res