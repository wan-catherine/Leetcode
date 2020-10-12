import collections

class Solution(object):
    def countSubgraphsForEachDiameter_(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        def get_max_diameter(mask0):
            ans = 0
            for i in range(n):
                if (1 << i) & mask0:
                    mask = mask0
                    bfs, bfs2 = [i], []
                    cur = 0
                    while bfs:
                        for i in bfs:
                            mask ^= 1 << i
                            for j in graph[i]:
                                if mask & (1 << j):
                                    bfs2.append(j)
                        cur += 1
                        bfs, bfs2 = bfs2, []
                    if mask:
                        return 0
                    ans = max(ans, cur - 1)
            return ans

        res = [0]*(n-1)
        for mask in range(1 << n):
            # filter out which contains only one node.
            if mask & (mask - 1) == 0:
                continue
            d = get_max_diameter(mask)
            if d:
                res[d-1] += 1
        return res

    def countSubgraphsForEachDiameter(self, n, edges):
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        def get_d(mask):
            ans = 0
            for i in range(n):
                if (1 << i) & mask == 0:
                    continue
                stack = [i]
                temp_mask = mask
                d = 0
                while stack:
                    new_stack = []
                    for j in stack:
                        temp_mask ^= (1 << j)
                        for k in graph[j]:
                            if temp_mask & (1 << k):
                                new_stack.append(k)
                    stack = new_stack
                    d += 1
                # this step is very important. it means for some mask, it might not be a tree.
                if temp_mask:
                    return 0
                ans = max(ans, d - 1)
            return ans

        res = [0] * (n-1)
        for mask in range(1 << n):
            if mask & (mask - 1) == 0:
                continue
            d = get_d(mask)
            if d :
                res[d-1] += 1
        return res