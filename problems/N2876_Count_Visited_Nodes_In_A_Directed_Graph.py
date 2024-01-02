from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        length = len(edges)
        indgrees = [0] * length
        for i in range(length):
            indgrees[edges[i]] += 1

        stack = []
        for i in range(length):
            if indgrees[i] == 0:
                stack.append(i)

        while stack:
            nstack = []
            for node in stack:
                indgrees[edges[node]] -= 1
                if indgrees[edges[node]] == 0:
                    nstack.append(edges[node])
            stack = nstack

        res = [0] * length
        for i in range(length):
            if indgrees[i] == 0 or res[i] != 0:
                continue
            j = i
            l = 1
            while edges[j] != i:
                j = edges[j]
                l += 1
            j = i
            while edges[j] != i:
                res[j] = l
                j = edges[j]
        def dfs(node):
            if res[node] != 0:
                return res[node]
            res[node] = dfs(edges[node]) + 1
            return res[node]

        for i in range(length):
            if indgrees[i] != 0:
                continue
            dfs(i)

        return res

